from django.test import TestCase
from django.utils import timezone

import pytest, unittest

class DatabaseTestCase(TestCase):
    def test_create_new_entry(self):
        """
        Can we create a new Django database entry?
        """
        print "create new entry placeholder"
        assert(True)

    @unittest.expectedFailure
    def test_create_duplicate_entry(self):
        """
        Can we create a duplicate database entry?
        """
        print "attempting to create duplicate entry"
        assert(False)

    def test_retrieve_entry(self):
        """
        Can we retrieve an existing database entry?
        """
        print "retrieve entry placeholder"
        assert(True)

    @unittest.expectedFailure
    def test_retrieve_nonexistent_entry(self):
        """
        Can we retrieve a non-existent database entry?
        """
        print "attempting non-existent entry access placeholder"
        assert(False)

    def test_update_entry(self):
        """
        Can we update an existing database entry?
        """
        print "update entry placeholder"
        assert(True)

    @unittest.expectedFailure
    def test_update_nonexistent_entry(self):
        """
        Can we update a non-existent database entry?
        """
        print "attempting non-existent entry update placeholder"
        assert(False)

    def test_delete_entry(self):
        """
        Can we delete an existing database entry?
        """
        print "delete entry placeholder"
        assert(True)

    @unittest.expectedFailure
    def test_delete_entry(self):
        """
        Can we delete a non-existent database entry?
        """
        print "attempting non-existent entry deletion placeholder"
        assert(False)
