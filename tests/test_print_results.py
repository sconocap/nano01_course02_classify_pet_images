"""Tests for print_results function.

Visual inspection only - no assertions.
"""

from print_results import print_results


def test_print_results_statistics_and_counts(
    adjusted_results4_isadog, statistics, capsys
):
    """Visual inspection: statistics and counts output."""
    print_results(adjusted_results4_isadog, statistics, "vgg")


def test_print_results_no_misclassifications_default(
    adjusted_results4_isadog, statistics, capsys
):
    """Visual inspection: default arguments (no misclassifications)."""
    print_results(adjusted_results4_isadog, statistics, "vgg")


def test_print_results_misclassifications_when_requested(
    adjusted_results4_isadog, statistics, capsys
):
    """Visual inspection: both flags True (misclassifications printed)."""
    print_results(adjusted_results4_isadog, statistics, "vgg", True, True)
