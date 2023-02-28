tree_names = {
    'P': 'paprastoji pušis',
    'Pk': 'kalninė pušis',
    'Pb': 'Bankso pušis',
    'Pj': 'juodoji pušis',
    'Kd': 'kedras',
    'E': 'eglė',
    'M': 'maumedis',
    'Pc': 'pocūgė',
    'Kn': 'kėnis',
    'Ks': 'kiti',
    'Ą': 'ąžuolas',
    'Ąr': 'raudonasis ąžuolas',
    'U': 'uosis',
    'K': 'klevas',
    'Sb': 'skroblas',
    'G': 'guoba',
    'S': 'skirpstas',
    'Bu': 'bukas',
    'V': 'vinkšna',
    'Kk': 'kiti kietieji',
    'B': 'beržas',
    'J': 'juodalksnis',
    'L': 'liepa',
    'D': 'drebulė',
    'Bt': 'baltalksnis',
    'T': 'tuopa',
    'Gl': 'gluosnis',
    'Bl': 'blindė',
    'Km': 'kiti minkštieji'
}

import pickle

liquid_t = {
    'P': 87,
    'Pk': 87,
    'Pb': 85,
    'Pj': 85,
    'Kd': 85,
    'E': 85,
    'M': 85,
    'Pc': 85,
    'Kn': 85,
    'Ks': 85,
    'Ą': 85,
    'Ąr': 84,
    'U': 85,
    'K': 85,
    'Sb': 85,
    'G': 85,
    'S': 85,
    'Bu': 85,
    'V': 85,
    'Kk': 85,
    'B': 83,
    'J': 83,
    'L': 85,
    'D': 87,
    'Bt': 88,
    'T': 85,
    'Gl': 85,
    'Bl': 85,
    'Km': 85
}

with open('../dictionary_1.pkl', 'wb') as pickle_out:
    pickle.dump(liquid_t, pickle_out)
    pickle.dump(tree_names, pickle_out)