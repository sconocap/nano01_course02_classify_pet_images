from calculates_results_stats import calculates_results_stats


def test_calculates_results_stats(adjusted_results4_isadog):
    result = calculates_results_stats(adjusted_results4_isadog)
    #print(result.items())
    assert result["n_images"] == 40
    assert result["n_dogs_img"] == 30
    assert result["n_notdogs_img"] == 10
    assert result["n_match"] == 35
    assert result["n_correct_dogs"] == 30
    assert result["n_correct_notdogs"] == 10
    assert result["n_correct_breed"] == 28
    assert result["pct_match"] == 87.5
    assert result["pct_correct_dogs"] == 100
    assert abs(result["pct_correct_breed"] - 93.33) < 0.01
    assert result["pct_correct_notdogs"] == 100