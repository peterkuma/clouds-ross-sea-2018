import h5py

def h5_save(filename):
    def f(data):
        with h5py.File(filename, 'a') as f:
            for k, v in data['datasets'].iteritems():
                try:
                    dataset = f[k]
                    n = dataset.len()
                    dataset.resize(n + v.shape[0], axis=0)
                    dataset[n:] = v
                except KeyError:
                    maxshape = list(v.shape)
                    maxshape[0] = None
                    dataset = f.create_dataset(k, data=v, maxshape=maxshape)
    return f
