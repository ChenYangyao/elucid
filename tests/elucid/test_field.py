from elucid.gen_util.field import ScalarField3D, VectorField3D, Field, ScalarField, VectorField
import pytest
import numpy as np

@pytest.fixture
def random_scalar_field():
    f = ScalarField3D(2**4)
    f.data[...] = np.random.default_rng(0).random(f.shape)
    return f

def test_generate_random_scaar_field(random_scalar_field: ScalarField3D):
    f = random_scalar_field
    print(f)
    
    assert isinstance(f, ScalarField3D)
    assert isinstance(f, ScalarField)
    assert isinstance(f, Field)
    
    assert isinstance(f.data, np.ndarray)
    assert f.data_shape == f.shape
    assert f.data_n_dims == f.n_dims
    assert f.shape == (16, 16, 16)
    assert f.n_dims == 3
    assert f.dtype is f.data.dtype
    
    assert isinstance(f.fft, ScalarField.FFTContext)
    f_in_k = f.fft.forward
    assert isinstance(f_in_k, ScalarField3D)
    assert isinstance(f_in_k.fft, ScalarField.FFTContext)
    f_in_x = f_in_k.fft.backward
    assert isinstance(f_in_x, ScalarField3D)
    
    assert f_in_k.fft_policy is f.fft_policy
    assert f_in_x.fft_policy is f.fft_policy
    assert np.abs(f_in_x.data - f.data).max() < 1.0e-5
    print(f_in_k)
    print(f_in_x)

@pytest.fixture
def random_vector_field():
    f = VectorField3D(2**4)
    f.data[...] = np.random.default_rng(0).random(f.data_shape)
    return f

def test_generate_random_vector_field(random_vector_field: VectorField3D):
    f = random_vector_field
    print(f)
    
    assert isinstance(f, VectorField3D)
    assert isinstance(f, VectorField)
    assert isinstance(f, Field)
    
    assert isinstance(f.data, np.ndarray)
    assert f.data_shape == f.shape + (3,)
    assert f.data_n_dims == f.n_dims + 1
    assert f.shape == (16, 16, 16)
    assert f.n_dims == 3
    assert f.n_comps == 3
    
    assert isinstance(f.fft, VectorField.FFTContext)
    f_in_k = f.fft.forward
    assert isinstance(f_in_k, VectorField3D)
    assert isinstance(f_in_k.fft, VectorField.FFTContext)
    f_in_x = f_in_k.fft.backward
    assert isinstance(f_in_x, VectorField3D)
    
    f_in_k_2 = np.stack([f.fft_policy.forward(c.data) for c in f.comps], 
                        axis=-1)
    print(f_in_k.data.shape, f_in_k_2.shape)
    assert np.abs(f_in_k.data - f_in_k_2).max() < 1.0e-5
    
    assert f_in_k.fft_policy is f.fft_policy
    assert f_in_x.fft_policy is f.fft_policy
    assert np.abs(f_in_x.data - f.data).max() < 1.0e-5
    print(f_in_k)
    print(f_in_x)