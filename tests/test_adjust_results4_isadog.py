from adjust_results4_isadog import adjust_results4_isadog

dogfile = "/Users/nico/Documents/masters_in_ai/capstones/intropyproject-classify-pet-images/src/intropyproject_classify_pet_images/data/dognames.txt"


def test_adjust_results4_isadog(results, adjusted_results4_isadog):
    """Test that adjust_results4_isadog adds is-a-dog flags to results."""
    adjust_results4_isadog(results, dogfile)
    assert results[ "cat_01.jpg"][3] == 0
    assert results[ "cat_01.jpg"][4] == 0
    assert results["Poodle_07927.jpg"][3] == 1
    assert results["Poodle_07927.jpg"][4] == 1
    # Deep compare all keys and values, order matters
    for k in results:
        assert results[k] == adjusted_results4_isadog[k], f"Mismatch for {k}: {results[k]} != {adjusted_results4_isadog[k]}"