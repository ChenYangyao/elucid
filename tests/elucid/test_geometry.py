import numpy as np
from elucid.geometry import frame
import pytest

@pytest.fixture
def frame_sdss_l500():
    return frame.SimFrameSdssL500()


def test_cvt_sim2j2k(frame_sdss_l500: frame.SimFrameSdssL500):
    frame = frame_sdss_l500
    
    x_sims = np.array([
    [332.63, 318.91, 63.53],       # Coma (Abell 1656)
    [321.13, 335.49, 51.64],       # Leo (Abell 1367)
    [254.91 , 221.74 , 44.49],     # Abell 1630
    [215.07, 198.16, 38.16],       # Abell 1564 
    ])

    x_j2ks = frame.pos_sim_to_j2k(x_sims)
    ras, decs, zs = frame.pos_j2k_to_ra_dec_z(x_j2ks)
    
    x_j2ks_back = frame.pos_ra_dec_z_to_j2k(ras, decs, zs)
    x_sims_back = frame.pos_j2k_to_sim(x_j2ks_back)
    
    assert np.abs(x_sims - x_sims_back).max() < 1.0e-1