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
                                'lssm.callbacks.CancelBatchException': ('callbacks.html#cancelbatchexception', 'lssm/callbacks.py'),
                                'lssm.callbacks.CancelEpochException': ('callbacks.html#cancelepochexception', 'lssm/callbacks.py'),
                                'lssm.callbacks.CancelFitException': ('callbacks.html#cancelfitexception', 'lssm/callbacks.py'),
                                'lssm.callbacks.DeviceCB': ('callbacks.html#devicecb', 'lssm/callbacks.py'),
                                'lssm.callbacks.DeviceCB.__init__': ('callbacks.html#devicecb.__init__', 'lssm/callbacks.py'),
                                'lssm.callbacks.DeviceCB.before_batch': ('callbacks.html#devicecb.before_batch', 'lssm/callbacks.py'),
                                'lssm.callbacks.DeviceCB.before_fit': ('callbacks.html#devicecb.before_fit', 'lssm/callbacks.py'),
                                'lssm.callbacks.LRFinderCB': ('callbacks.html#lrfindercb', 'lssm/callbacks.py'),
                                'lssm.callbacks.LRFinderCB.__init__': ('callbacks.html#lrfindercb.__init__', 'lssm/callbacks.py'),
                                'lssm.callbacks.LRFinderCB.after_batch': ('callbacks.html#lrfindercb.after_batch', 'lssm/callbacks.py'),
                                'lssm.callbacks.LRFinderCB.before_fit': ('callbacks.html#lrfindercb.before_fit', 'lssm/callbacks.py'),
                                'lssm.callbacks.LRFinderCB.cleanup_fit': ('callbacks.html#lrfindercb.cleanup_fit', 'lssm/callbacks.py'),
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
                                'lssm.callbacks.to_cpu': ('callbacks.html#to_cpu', 'lssm/callbacks.py'),
                                'lssm.callbacks.to_device': ('callbacks.html#to_device', 'lssm/callbacks.py')},
            'lssm.dataloaders': { 'lssm.dataloaders.CrossSpectraDataset': ('dataloaders.html#crossspectradataset', 'lssm/dataloaders.py'),
                                  'lssm.dataloaders.CrossSpectraDataset.__getitem__': ( 'dataloaders.html#crossspectradataset.__getitem__',
                                                                                        'lssm/dataloaders.py'),
                                  'lssm.dataloaders.CrossSpectraDataset.__init__': ( 'dataloaders.html#crossspectradataset.__init__',
                                                                                     'lssm/dataloaders.py'),
                                  'lssm.dataloaders.CrossSpectraDataset.__len__': ( 'dataloaders.html#crossspectradataset.__len__',
                                                                                    'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralDataset': ('dataloaders.html#spectraldataset', 'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralDataset.__getitem__': ( 'dataloaders.html#spectraldataset.__getitem__',
                                                                                    'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralDataset.__init__': ( 'dataloaders.html#spectraldataset.__init__',
                                                                                 'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralDataset.__len__': ( 'dataloaders.html#spectraldataset.__len__',
                                                                                'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralEmbeddingDataset': ( 'dataloaders.html#spectralembeddingdataset',
                                                                                 'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralEmbeddingDataset.__getitem__': ( 'dataloaders.html#spectralembeddingdataset.__getitem__',
                                                                                             'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralEmbeddingDataset.__init__': ( 'dataloaders.html#spectralembeddingdataset.__init__',
                                                                                          'lssm/dataloaders.py'),
                                  'lssm.dataloaders.SpectralEmbeddingDataset.__len__': ( 'dataloaders.html#spectralembeddingdataset.__len__',
                                                                                         'lssm/dataloaders.py'),
                                  'lssm.dataloaders.get_dls': ('dataloaders.html#get_dls', 'lssm/dataloaders.py')},
            'lssm.hooks': { 'lssm.hooks.Hook': ('hooks.html#hook', 'lssm/hooks.py'),
                            'lssm.hooks.Hook.__del__': ('hooks.html#hook.__del__', 'lssm/hooks.py'),
                            'lssm.hooks.Hook.__init__': ('hooks.html#hook.__init__', 'lssm/hooks.py'),
                            'lssm.hooks.Hook.remove': ('hooks.html#hook.remove', 'lssm/hooks.py'),
                            'lssm.hooks.ToyCNN': ('hooks.html#toycnn', 'lssm/hooks.py'),
                            'lssm.hooks.ToyCNN.__init__': ('hooks.html#toycnn.__init__', 'lssm/hooks.py'),
                            'lssm.hooks.ToyCNN.forward': ('hooks.html#toycnn.forward', 'lssm/hooks.py')},
            'lssm.learner': { 'lssm.learner.Learner': ('learner.html#learner', 'lssm/learner.py'),
                              'lssm.learner.Learner.__getattr__': ('learner.html#learner.__getattr__', 'lssm/learner.py'),
                              'lssm.learner.Learner.__init__': ('learner.html#learner.__init__', 'lssm/learner.py'),
                              'lssm.learner.Learner._batch_preds': ('learner.html#learner._batch_preds', 'lssm/learner.py'),
                              'lssm.learner.Learner._fit': ('learner.html#learner._fit', 'lssm/learner.py'),
                              'lssm.learner.Learner._one_batch': ('learner.html#learner._one_batch', 'lssm/learner.py'),
                              'lssm.learner.Learner._one_epoch': ('learner.html#learner._one_epoch', 'lssm/learner.py'),
                              'lssm.learner.Learner.callback': ('learner.html#learner.callback', 'lssm/learner.py'),
                              'lssm.learner.Learner.fit': ('learner.html#learner.fit', 'lssm/learner.py'),
                              'lssm.learner.Learner.get_preds': ('learner.html#learner.get_preds', 'lssm/learner.py'),
                              'lssm.learner.Learner.one_epoch': ('learner.html#learner.one_epoch', 'lssm/learner.py'),
                              'lssm.learner.Learner.training': ('learner.html#learner.training', 'lssm/learner.py'),
                              'lssm.learner.lr_find': ('learner.html#lr_find', 'lssm/learner.py'),
                              'lssm.learner.with_cbs': ('learner.html#with_cbs', 'lssm/learner.py'),
                              'lssm.learner.with_cbs.__call__': ('learner.html#with_cbs.__call__', 'lssm/learner.py'),
                              'lssm.learner.with_cbs.__init__': ('learner.html#with_cbs.__init__', 'lssm/learner.py')},
            'lssm.loading': { 'lssm.loading.download': ('loading.html#download', 'lssm/loading.py'),
                              'lssm.loading.get_spectra_pair_idxs': ('loading.html#get_spectra_pair_idxs', 'lssm/loading.py'),
                              'lssm.loading.load_mir_kex_spike': ('loading.html#load_mir_kex_spike', 'lssm/loading.py'),
                              'lssm.loading.load_mir_ring_trial': ('loading.html#load_mir_ring_trial', 'lssm/loading.py'),
                              'lssm.loading.load_nir_kex_spike': ('loading.html#load_nir_kex_spike', 'lssm/loading.py'),
                              'lssm.loading.load_ossl': ('loading.html#load_ossl', 'lssm/loading.py')},
            'lssm.models': { 'lssm.models.CVAE': ('models.html#cvae', 'lssm/models.py'),
                             'lssm.models.CVAE.__init__': ('models.html#cvae.__init__', 'lssm/models.py'),
                             'lssm.models.CVAE.forward': ('models.html#cvae.forward', 'lssm/models.py'),
                             'lssm.models.CVAE.reparameterize': ('models.html#cvae.reparameterize', 'lssm/models.py'),
                             'lssm.models.Decoder': ('models.html#decoder', 'lssm/models.py'),
                             'lssm.models.Decoder.__init__': ('models.html#decoder.__init__', 'lssm/models.py'),
                             'lssm.models.Decoder.forward': ('models.html#decoder.forward', 'lssm/models.py'),
                             'lssm.models.Encoder': ('models.html#encoder', 'lssm/models.py'),
                             'lssm.models.Encoder.__init__': ('models.html#encoder.__init__', 'lssm/models.py'),
                             'lssm.models.Encoder.forward': ('models.html#encoder.forward', 'lssm/models.py'),
                             'lssm.models.GeneralRelu': ('models.html#generalrelu', 'lssm/models.py'),
                             'lssm.models.GeneralRelu.__init__': ('models.html#generalrelu.__init__', 'lssm/models.py'),
                             'lssm.models.GeneralRelu.forward': ('models.html#generalrelu.forward', 'lssm/models.py'),
                             'lssm.models.ResBlock': ('models.html#resblock', 'lssm/models.py'),
                             'lssm.models.ResBlock.__init__': ('models.html#resblock.__init__', 'lssm/models.py'),
                             'lssm.models.ResBlock.forward': ('models.html#resblock.forward', 'lssm/models.py'),
                             'lssm.models.ResBlockUp': ('models.html#resblockup', 'lssm/models.py'),
                             'lssm.models.ResBlockUp.__init__': ('models.html#resblockup.__init__', 'lssm/models.py'),
                             'lssm.models.ResBlockUp.forward': ('models.html#resblockup.forward', 'lssm/models.py'),
                             'lssm.models.conv': ('models.html#conv', 'lssm/models.py'),
                             'lssm.models.conv_block': ('models.html#conv_block', 'lssm/models.py'),
                             'lssm.models.init_weights': ('models.html#init_weights', 'lssm/models.py'),
                             'lssm.models.plot_func': ('models.html#plot_func', 'lssm/models.py')},
            'lssm.preprocessing': { 'lssm.preprocessing.BaselineALS': ('preprocessing.html#baselineals', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.BaselineALS.__init__': ( 'preprocessing.html#baselineals.__init__',
                                                                                 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.BaselineALS._baseline_als': ( 'preprocessing.html#baselineals._baseline_als',
                                                                                      'lssm/preprocessing.py'),
                                    'lssm.preprocessing.BaselineALS.fit': ('preprocessing.html#baselineals.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.BaselineALS.transform': ( 'preprocessing.html#baselineals.transform',
                                                                                  'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ContinuumRemoval': ('preprocessing.html#continuumremoval', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ContinuumRemoval.__init__': ( 'preprocessing.html#continuumremoval.__init__',
                                                                                      'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ContinuumRemoval.fit': ( 'preprocessing.html#continuumremoval.fit',
                                                                                 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.ContinuumRemoval.transform': ( 'preprocessing.html#continuumremoval.transform',
                                                                                       'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Interpolate': ('preprocessing.html#interpolate', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Interpolate.__init__': ( 'preprocessing.html#interpolate.__init__',
                                                                                 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Interpolate.fit': ('preprocessing.html#interpolate.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Interpolate.transform': ( 'preprocessing.html#interpolate.transform',
                                                                                  'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Log1p': ('preprocessing.html#log1p', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Log1p.fit': ('preprocessing.html#log1p.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.Log1p.transform': ('preprocessing.html#log1p.transform', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.MeanCenter': ('preprocessing.html#meancenter', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.MeanCenter.fit': ('preprocessing.html#meancenter.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.MeanCenter.transform': ( 'preprocessing.html#meancenter.transform',
                                                                                 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.MinScaler': ('preprocessing.html#minscaler', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.MinScaler.fit': ('preprocessing.html#minscaler.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.MinScaler.transform': ( 'preprocessing.html#minscaler.transform',
                                                                                'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SNV': ('preprocessing.html#snv', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SNV.fit': ('preprocessing.html#snv.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SNV.transform': ('preprocessing.html#snv.transform', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeDiff': ('preprocessing.html#spikediff', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeDiff.__init__': ( 'preprocessing.html#spikediff.__init__',
                                                                               'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeDiff._get_diffs_idx': ( 'preprocessing.html#spikediff._get_diffs_idx',
                                                                                     'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeDiff._get_levels_reps': ( 'preprocessing.html#spikediff._get_levels_reps',
                                                                                       'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeDiff.fit': ('preprocessing.html#spikediff.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeDiff.transform': ( 'preprocessing.html#spikediff.transform',
                                                                                'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeMean': ('preprocessing.html#spikemean', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeMean.__init__': ( 'preprocessing.html#spikemean.__init__',
                                                                               'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeMean._get_smp_names': ( 'preprocessing.html#spikemean._get_smp_names',
                                                                                     'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeMean.fit': ('preprocessing.html#spikemean.fit', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.SpikeMean.transform': ( 'preprocessing.html#spikemean.transform',
                                                                                'lssm/preprocessing.py'),
                                    'lssm.preprocessing.TakeDerivative': ('preprocessing.html#takederivative', 'lssm/preprocessing.py'),
                                    'lssm.preprocessing.TakeDerivative.__init__': ( 'preprocessing.html#takederivative.__init__',
                                                                                    'lssm/preprocessing.py'),
                                    'lssm.preprocessing.TakeDerivative.fit': ( 'preprocessing.html#takederivative.fit',
                                                                               'lssm/preprocessing.py'),
                                    'lssm.preprocessing.TakeDerivative.transform': ( 'preprocessing.html#takederivative.transform',
                                                                                     'lssm/preprocessing.py'),
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
                                 'lssm.transforms.SNVTfm': ('transforms.html#snvtfm', 'lssm/transforms.py'),
                                 'lssm.transforms.SNVTfm.__call__': ('transforms.html#snvtfm.__call__', 'lssm/transforms.py'),
                                 'lssm.transforms.SNVTfm.__init__': ('transforms.html#snvtfm.__init__', 'lssm/transforms.py'),
                                 'lssm.transforms.SNVTfm._apply_snv': ('transforms.html#snvtfm._apply_snv', 'lssm/transforms.py'),
                                 'lssm.transforms.StatsTfm': ('transforms.html#statstfm', 'lssm/transforms.py'),
                                 'lssm.transforms.StatsTfm.__call__': ('transforms.html#statstfm.__call__', 'lssm/transforms.py'),
                                 'lssm.transforms.StatsTfm.__init__': ('transforms.html#statstfm.__init__', 'lssm/transforms.py'),
                                 'lssm.transforms._resizeTfm': ('transforms.html#_resizetfm', 'lssm/transforms.py')},
            'lssm.visualization': {'lssm.visualization.plot_spectra': ('visualization.html#plot_spectra', 'lssm/visualization.py')}}}
