import unittest

from ..src import access, fields, lifecycle, location


class TestContracts(unittest.TestCase):
    def test_lifecycle_values_are_integer_milliseconds(self):
        self.assertEqual(lifecycle.FREE_AUTHENTICATION_PERIOD_MS, 302_400_000)
        self.assertEqual(lifecycle.PAID_AUTHENTICATION_PERIOD_MS, 907_200_000)
        self.assertEqual(lifecycle.DEFAULT_RESOURCE_RETENTION_MS, 907_200_000)
        self.assertEqual(lifecycle.ACCESS_TOKEN_ALL_LIFETIME_MS, 43_200_000)
        self.assertEqual(lifecycle.ACCESS_TOKEN_ALL_IDLE_TIMEOUT_MS, 10_800_000)
        self.assertIsInstance(lifecycle.DEFAULT_RESOURCE_RETENTION_MS, int)

    def test_storage_contracts(self):
        self.assertEqual(fields.TTL_ATTRIBUTE_NAME, "ttl_expires_at")
        self.assertEqual(lifecycle.S3_RESOURCE_RETENTION_DAYS, 11)

    def test_access_and_location_values(self):
        self.assertEqual(access.INITIAL_ACCESS_PERMISSIONS, ("read", "post"))
        self.assertEqual(
            {
                access.ACCESS_PERMISSION_READ,
                access.ACCESS_PERMISSION_POST,
                access.ACCESS_PERMISSION_ALL,
            },
            {"read", "post", "all"},
        )
        self.assertEqual(location.LOCATION_MODES, {"off", "on"})


if __name__ == "__main__":
    unittest.main()