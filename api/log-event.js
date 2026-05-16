import { kv } from '@vercel/kv';
import crypto from 'crypto';

export default async function handler(req, res) {
    // Only allow POST requests for clinical data entry
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    try {
        const { type, timestamp, metadata } = req.body;

        // Validation for deterministic entry
        if (!type || !timestamp) {
            return res.status(400).json({ error: 'Type and timestamp are required' });
        }

        // 1. Retrieve the last entry to get the 'previousHash' (The Chain Link)
        const latestEntry = await kv.get('ledger:latest');
        const previousHash = latestEntry ? latestEntry.hash : null;

        // 2. Define the secret key from your Vercel Environment Variables
        // Defaults to 'jubilee-protocol-key' if not set
        const secret = process.env.JUBILEE_PROTOCOL_KEY || 'jubilee-protocol-key';

        // 3. Construct the event object
        const currentEvent = { 
            type, 
            timestamp, 
            previousHash,
            metadata: metadata || {} 
        };

        // 4. Compute the HMAC Hash (The Secure Seal)
        const hmac = crypto.createHmac('sha256', secret);
        hmac.update(JSON.stringify(currentEvent));
        const currentHash = hmac.digest('hex');

        // 5. Build the final record
        const finalRecord = { ...currentEvent, hash: currentHash };

        // 6. Save to Vercel KV (Atomic Updates)
        // 'rpush' adds it to the list; 'set' updates the pointer for the next entry
        await kv.rpush('ledger:entries', JSON.stringify(finalRecord));
        await kv.set('ledger:latest', finalRecord);

        // Success Response
        return res.status(200).json({ 
            status: 'VERIFIED', 
            hash: currentHash,
            message: 'Event appended to permanent ledger.' 
        });

    } catch (error) {
        console.error(`Clinical Audit Error: ${error.message}`);
        return res.status(500).json({ error: 'Internal Server Error - Check KV Connection' });
    }
}
