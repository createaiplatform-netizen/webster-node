import { kv } from '@vercel/kv';

export default async function handler(req, res) {
    try {
        const logs = await kv.lrange('ledger:entries', -10, -1);
        return res.status(200).json(logs.map(l => typeof l === 'string' ? JSON.parse(l) : l));
    } catch (e) {
        return res.status(200).json([]);
    }
}
