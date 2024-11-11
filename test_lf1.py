from LFTracer import LFTracer
from sha256 import generate_hash


def test_lf_sha256():
    with LFTracer(target_func = ["generate_hash", "_sigma0"]) as traced:
        encoded = "mysalt".encode()
        generate_hash(encoded).hex()

    # print(traced.getLFMap())
    answer1 = {'generate_hash': {15: 1, 20: 1, 22: 1, 23: 1, 28: 1, 29: 1, 30: 50, 31: 49, 33: 1, 35: 1, 38: 1, 39: 2, 40: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1, 53: 2, 55: 1, 56: 65, 57: 64, 61: 16, 63: 48, 64: 48, 65: 48, 66: 48, 69: 48, 70: 48, 72: 1, 75: 1, 76: 1, 77: 1, 78: 1, 79: 1, 80: 1, 81: 1, 82: 1, 85: 65, 86: 192, 87: 128, 89: 64, 91: 64, 92: 64, 93: 64, 94: 64, 95: 64, 96: 64, 97: 64, 98: 64, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1, 110: 8, 111: 2, 112: 2, 113: 2}, '_sigma0': {115: 48, 117: 144, 118: 48, 119: 48, 120: 96}}
    answer2 = {'_sigma0': {'num_visited_lines': 5, 'total_visitied_counts': 384}, 'generate_hash': {'num_visited_lines': 65, 'total_visitied_counts': 1547}}
    assert traced.getLFMap() == answer1
    assert traced.getLFStat() == answer2


if __name__ == '__main__':
    test_lf_sha256()
