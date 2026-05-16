import crypto from 'crypto';
import fs from 'fs';

export default async function handler(req, res) {
    if (req.method !== 'POST') {
        res.status(405).json({ error: 'Method Not Allowed' });
        return;
    }

    try {
        const { type, timestamp } = req.body;

        if (!type || !timestamp) {
            res.status(400).json({ error: 'Type and timestamp are required' });
            return;
        }

        const ledgerPath = '/tmp/ledger.json';

        // Get the previous hash from the ledger
        const previousHash = fs.existsSync(ledgerPath)
            ? JSON.parse(fs.readFileSync(ledgerPath, 'utf8')).slice(-1)[0]?.hash
            : null;

        // Construct the current event
        const currentEvent = { type, timestamp, previousHash };
        const currentHash = computeHMACHash(currentEvent);

        // Append the new event with its hash to the ledger
        const ledgerData = fs.existsSync(ledgerPath) ? JSON.parse(fs.readFileSync(ledgerPath, 'utf8')) : [];
        ledgerData.push({ ...currentEvent, hash: currentHash });

        // Write to /tmp/ledger.json for serverless environments
        fs.writeFileSync(ledgerPath, JSON.stringify(ledgerData, null, 2));

        res.status(200).json({ message: 'Event logged successfully', hash: currentHash });
    } catch (error) {
        console.error(`Error logging event: ${error.message}`);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}

// Helper function to compute HMAC hash for cryptographic linking
function computeHMACHash(event, secretKey = 'jubilee-protocol-key') {
    const hmac = crypto.createHmac('sha256', secretKey);
    hmac.update(JSON.stringify(event));
    return hmac.digest('hex');
}