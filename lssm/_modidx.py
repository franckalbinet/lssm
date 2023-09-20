# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/lssm',
                'doc_host': 'https://franckalbinet.github.io',
                'git_url': 'https://github.com/franckalbinet/lssm',
                'lib_path': 'lssm'},
  'syms': { 'lssm.callbacks': { 'lssm.callbacks.BaseSchedCB': ('callbacks.html#baseschedcb', 'lssm/callbacks.py'),
                                'lssm.callbacks.BaseSchedCB.__init__': ('callbacks.html#baseschedcb.__init__', 'lssm/callbacks.py'),
                                'lssm.callbacks.BaseSchedCB._step': ('callbacks.html#baseschedcb._step', 'lssm/callbacks.py'),
                                'lssm.callbacks.BaseSchedCB.before_fit': ('callbacks.html#baseschedcb.before_fit', 'lssm/callbacks.py'),
                                'lssm.callbacks.BatchSchedCB': ('callbacks.html#batchschedcb', 'lssm/callbacks.py'),
                                'lssm.callbacks.BatchSchedCB.after_batch': ('callbacks.html#batchschedcb.after_batch', 'lssm/callbacks.py'),
                                'lssm.callbacks.BatchTransformCB': ('callbacks.html#batchtransformcb', 'lssm/callbacks.py'),
                                'lssm.callbacks.BatchTransformCB.__init__': ( 'callbacks.html#batchtransformcb.__init__',
                                                                              'lssm/callbacks.py'),
                                'lssm.callbacks.BatchTransformCB.before_batch': ( 'callbacks.html#batchtransformcb.before_batch',
                                                                                  'lssm/callbacks.py'),
                                'lssm.callbacks.Callback': ('callbacks.html#callback', 'lssm/callbacks.py'),
                                'lssm.callbacks.DeviceCB': ('callbacks.html#devicecb', 'lssm/callbacks.py'),
                                'lssm.callbacks.DeviceCB.__init__': ('callbacks.html#devicecb.__init__', 'lssm/callbacks.py'),
                                'lssm.callbacks.DeviceCB.before_batch': ('callbacks.html#devicecb.before_batch', 'lssm/callbacks.py'),
                                'lssm.callbacks.DeviceCB.before_fit': ('callbacks.html#devicecb.before_fit', 'lssm/callbacks.py'),
                                'lssm.callbacks.MetricsCB': ('callbacks.html#metricscb', 'lssm/callbacks.py'),
                                'lssm.callbacks.MetricsCB.__init__': ('callbacks.html#metricscb.__init__', 'lssm/callbacks.py'),
                                'lssm.callbacks.MetricsCB._log': ('callbacks.html#metricscb._log', 'lssm/callbacks.py'),
                                'lssm.callbacks.MetricsCB.after_batch': ('callbacks.html#metricscb.after_batch', 'lssm/callbacks.py'),
                                'lssm.callbacks.MetricsCB.after_epoch': ('callbacks.html#metricscb.after_epoch', 'lssm/callbacks.py'),
                                'lssm.callbacks.MetricsCB.before_epoch': ('callbacks.html#metricscb.before_epoch', 'lssm/callbacks.py'),
                                'lssm.callbacks.MetricsCB.before_fit': ('callbacks.html#metricscb.before_fit', 'lssm/callbacks.py'),
                                'lssm.callbacks.ProgressCB': ('callbacks.html#progresscb', 'lssm/callbacks.py'),
                                'lssm.callbacks.ProgressCB.__init__': ('callbacks.html#progresscb.__init__', 'lssm/callbacks.py'),
                                'lssm.callbacks.ProgressCB._log': ('callbacks.html#progresscb._log', 'lssm/callbacks.py'),
                                'lssm.callbacks.ProgressCB.after_batch': ('callbacks.html#progresscb.after_batch', 'lssm/callbacks.py'),
                                'lssm.callbacks.ProgressCB.after_epoch': ('callbacks.html#progresscb.after_epoch', 'lssm/callbacks.py'),
                                'lssm.callbacks.ProgressCB.before_epoch': ('callbacks.html#progresscb.before_epoch', 'lssm/callbacks.py'),
                                'lssm.callbacks.ProgressCB.before_fit': ('callbacks.html#progresscb.before_fit', 'lssm/callbacks.py'),
                                'lssm.callbacks.SingleBatchCB': ('callbacks.html#singlebatchcb', 'lssm/callbacks.py'),
                                'lssm.callbacks.SingleBatchCB.after_batch': ( 'callbacks.html#singlebatchcb.after_batch',
                                                                              'lssm/callbacks.py'),
                                'lssm.callbacks.TrainCB': ('callbacks.html#traincb', 'lssm/callbacks.py'),
                                'lssm.callbacks.TrainCB.__init__': ('callbacks.html#traincb.__init__', 'lssm/callbacks.py'),
                                'lssm.callbacks.TrainCB.backward': ('callbacks.html#traincb.backward', 'lssm/callbacks.py'),
                                'lssm.callbacks.TrainCB.get_loss': ('callbacks.html#traincb.get_loss', 'lssm/callbacks.py'),
                                'lssm.callbacks.TrainCB.predict': ('callbacks.html#traincb.predict', 'lssm/callbacks.py'),
                                'lssm.callbacks.TrainCB.step': ('callbacks.html#traincb.step', 'lssm/callbacks.py'),
                                'lssm.callbacks.TrainCB.zero_grad': ('callbacks.html#traincb.zero_grad', 'lssm/callbacks.py'),
                                'lssm.callbacks.run_cbs': ('callbacks.html#run_cbs', 'lssm/callbacks.py'),
                                'lssm.callbacks.to_device': ('callbacks.html#to_device', 'lssm/callbacks.py')},
            'lssm.dataloaders': { 'lssm.dataloaders.SpectralDataset': ('dataloaders.html#spectraldataset', 'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralDataset.__getitem__': ( 'dataloaders.html#spectraldataset.__getitem__',
                                                                                    'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralDataset.__init__': ( 'dataloaders.html#spectraldataset.__init__',
                                                                                 'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralDataset.__len__': ( 'dataloaders.html#spectraldataset.__len__',
                                                                                'lssm/dataloaders.py'),
                                  'lssm.dataloaders.get_dls': ('dataloaders.html#get_dls', 'lssm/dataloaders.py')},
            'lssm.learner': { 'lssm.learner.CancelBatchException': ('learner.html#cancelbatchexception', 'lssm/learner.py'),
                              'lssm.learner.CancelEpochException': ('learner.html#cancelepochexception', 'lssm/learner.py'),
                              'lssm.learner.CancelFitException': ('learner.html#cancelfitexception', 'lssm/learner.py'),
                              'lssm.learner.Learner': ('learner.html#learner', 'lssm/learner.py'),
                              'lssm.learner.Learner.__getattr__': ('learner.html#learner.__getattr__', 'lssm/learner.py'),
                              'lssm.learner.Learner.__init__': ('learner.html#learner.__init__', 'lssm/learner.py'),
                              'lssm.learner.Learner._fit': ('learner.html#learner._fit', 'lssm/learner.py'),
                              'lssm.learner.Learner._one_batch': ('learner.html#learner._one_batch', 'lssm/learner.py'),
                              'lssm.learner.Learner._one_epoch': ('learner.html#learner._one_epoch', 'lssm/learner.py'),
                              'lssm.learner.Learner.callback': ('learner.html#learner.callback', 'lssm/learner.py'),
                              'lssm.learner.Learner.fit': ('learner.html#learner.fit', 'lssm/learner.py'),
                              'lssm.learner.Learner.one_epoch': ('learner.html#learner.one_epoch', 'lssm/learner.py'),
                              'lssm.learner.Learner.training': ('learner.html#learner.training', 'lssm/learner.py'),
                              'lssm.learner.to_cpu': ('learner.html#to_cpu', 'lssm/learner.py'),
                              'lssm.learner.with_cbs': ('learner.html#with_cbs', 'lssm/learner.py'),
                              'lssm.learner.with_cbs.__call__': ('learner.html#with_cbs.__call__', 'lssm/learner.py'),
                              'lssm.learner.with_cbs.__init__': ('learner.html#with_cbs.__init__', 'lssm/learner.py')},
            'lssm.loading': { 'lssm.loading.download': ('loading.html#download', 'lssm/loading.py'),
                              'lssm.loading.load_ossl': ('loading.html#load_ossl', 'lssm/loading.py')},
            'lssm.preprocessing': { 'lssm.preprocessing.ContinuumRemoval': ('preprocessing.html#continuumremoval', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ContinuumRemoval.__init__': ( 'preprocessing.html#continuumremoval.__init__',
                                                                                      'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ContinuumRemoval.fit': ( 'preprocessing.html#continuumremoval.fit',
                                                                                 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ContinuumRemoval.transform': ( 'preprocessing.html#continuumremoval.transform',
                                                                                       'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Log1p': ('preprocessing.html#log1p', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Log1p.fit': ('preprocessing.html#log1p.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Log1p.transform': ('preprocessing.html#log1p.transform', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SNV': ('preprocessing.html#snv', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SNV.fit': ('preprocessing.html#snv.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SNV.transform': ('preprocessing.html#snv.transform', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ToAbsorbance': ('preprocessing.html#toabsorbance', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ToAbsorbance.__init__': ( 'preprocessing.html#toabsorbance.__init__',
                                                                                  'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ToAbsorbance.fit': ('preprocessing.html#toabsorbance.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ToAbsorbance.transform': ( 'preprocessing.html#toabsorbance.transform',
                                                                                   'lssm/preprocessing.py')},
            'lssm.transforms': { 'lssm.transforms.GADFTfm': ('transforms.html#gadftfm', 'lssm/transforms.py'),
                                 'lssm.transforms.GADFTfm.__call__': ('transforms.html#gadftfm.__call__', 'lssm/transforms.py'),
                                 'lssm.transforms.GADFTfm.__init__': ('transforms.html#gadftfm.__init__', 'lssm/transforms.py'),
                                 'lssm.transforms.GADFTfm.rescale': ('transforms.html#gadftfm.rescale', 'lssm/transforms.py'),
                                 'lssm.transforms.StatsTfm': ('transforms.html#statstfm', 'lssm/transforms.py'),
                                 'lssm.transforms.StatsTfm.__call__': ('transforms.html#statstfm.__call__', 'lssm/transforms.py'),
                                 'lssm.transforms.StatsTfm.__init__': ('transforms.html#statstfm.__init__', 'lssm/transforms.py'),
                                 'lssm.transforms._resizeTfm': ('transforms.html#_resizetfm', 'lssm/transforms.py')},
            'lssm.visualization': {'lssm.visualization.plot_spectra': ('visualization.html#plot_spectra', 'lssm/visualization.py')}}}
