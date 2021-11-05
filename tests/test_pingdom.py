"""
Test module for pingdom formatter.
"""

import unittest

import httpx
import nio

from .start import BOT_URL, FULL_ID, KEY, MATRIX_ID, MATRIX_PW, MATRIX_URL


class PingdomFormatterTest(unittest.IsolatedAsyncioTestCase):
    """Grafana formatter test class."""

    async def test_pingdom_http_body(self):
        """Send a markdown message, and check the result."""
        messages = []
        client = nio.AsyncClient(MATRIX_URL, MATRIX_ID)

        await client.login(MATRIX_PW)
        room = await client.room_create()

        with open("tests/example_pingdom_http.json") as f:
            example_pingdom_request = f.read()
        self.assertEqual(
            httpx.post(
                f"{BOT_URL}/{room.room_id}",
                params={"formatter": "pingdom", "key": KEY},
                content=example_pingdom_request,
            ).json(),
            {"status": 200, "ret": "OK"},
        )

        sync = await client.sync()
        messages = await client.room_messages(room.room_id, sync.next_batch)
        await client.close()

        message = messages.chunk[0]
        self.assertEqual(message.sender, FULL_ID)
        self.assertEqual(
            message.body,
            "#### [Alerting] Panel Title alert\nNotification Message\n\n* Count: 1\n",
        )
