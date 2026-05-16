import { kv } from '@vercel/kv';
import crypto from 'crypto';

export default async function handler(req, res) {
    if (req.method !== 'POST') return res.status(405).send('Method Not Allowed');
    try {
        const { type, timestamp } = req.body;
        const secret = process.env.JUBILEE_PROTOCOL_KEY || 'jubilee-protocol-key';
        
        // This pulls the last link in the chain from the KV database
        const latest = await kv.get('ledger:latest').catch(() => null);
        const previousHash = latest ? latest.hash : null;

        const currentEvent = { type, timestamp, previousHash };
        const hmac = crypto.createHmac('sha256', secret);
        hmac.update(JSON.stringify(currentEvent));
        const hash = hmac.digest('hex');

        const record = { ...currentEvent, hash };
        
        // Permanent Atomic Commit
        await Promise.all([
            kv.rpush('ledger:entries', JSON.stringify(record)),
            kv.set('ledger:latest', record)
        ]);

        return res.status(200).json({ status: 'VERIFIED', hash });
    } catch (e) {
        return res.status(500).json({ error: 'Database Link Pending' });
    }
}
