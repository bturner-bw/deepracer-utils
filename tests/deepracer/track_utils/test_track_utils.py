from deepracer.tracks import GeometryUtils
import numpy as np

class TestGeometryUtils:
    def test_vector(self):
        assert np.all([23, 67] == GeometryUtils.vector([50, 100], [27, 33]))

    def test_angle_zero(self):
        assert 0.0 == GeometryUtils.get_angle([1, 1], [1, 1])

    def test_angle_ninety(self):
        assert 90.0 == GeometryUtils.get_angle([1, 1], [-1, 1])

    def test_angle_np_array_minus_forty_five(self):
        assert -45.0 == GeometryUtils.get_angle(np.array([1, 1]), np.array([1, 0]))

    def test_angle_one_eighty(self):
        assert 180.0 == GeometryUtils.get_angle([-1, -1], [1, 1])

    def test_vector_length_one(self):
        assert 1.0 == GeometryUtils.get_vector_length([0, 1])

    def test_vector_np_array_length_three(self):
        assert 3.0 == GeometryUtils.get_vector_length(np.array([3, 0]))

    def test_normalize_vector_length_three(self):
        assert np.all([1.0, 0.0] == GeometryUtils.normalize_vector(np.array([3, 0])))

    def test_normalize_vector_length_ten(self):
        assert np.all([0.0, 1.0] == GeometryUtils.normalize_vector([0, 10]))

    def test_perpendicular_vector(self):
        assert np.all([0.0, 1.0] == GeometryUtils.perpendicular_vector([1.0, 0.0]))

    def test_perpendicular_normalized_vector_to_straight_line(self):
        assert np.all([0.0, 1.0] == GeometryUtils.perpendicular_normalized_vector_to_straight_line([5.0, 0.0]))