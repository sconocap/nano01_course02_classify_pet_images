import sys
from unittest.mock import patch

from get_input_args import get_input_args


def test_no_args_uses_defaults():
    """Test that get_input_args returns default values when no arguments are provided."""
    with patch.object(sys, "argv", ["script_name"]):
        result = get_input_args()
        assert result.dir == "pet_images/"
        assert result.arch == "vgg"
        assert result.dogfile == "dognames.txt"


def test_all_args_provided():
    """Test that get_input_args correctly parses all provided arguments."""
    with patch.object(
        sys,
        "argv",
        [
            "script_name",
            "--dir",
            "custom_images/",
            "--arch",
            "resnet",
            "--dogfile",
            "custom_dognames.txt",
        ],
    ):
        result = get_input_args()
        assert result.dir == "custom_images/"
        assert result.arch == "resnet"
        assert result.dogfile == "custom_dognames.txt"


def test_partial_args_uses_defaults():
    """Test that get_input_args uses defaults for missing arguments."""
    with patch.object(sys, "argv", ["script_name", "--arch", "alexnet"]):
        result = get_input_args()
        assert result.dir == "pet_images/"  # default
        assert result.arch == "alexnet"  # provided
        assert result.dogfile == "dognames.txt"  # default
