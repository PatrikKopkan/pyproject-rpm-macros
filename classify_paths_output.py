PARAMETRIZED_EXPECTED_OUTPUT = {
    "requests": {'executables': {'files': []},
                 'metadata': {'dirs': ['/usr/lib/python3.7/site-packages/requests-2.22.0.dist-info/'],
                              'docs': [],
                              'files': sorted(['/usr/lib/python3.7/site-packages/requests-2.22.0.dist-info/LICENSE',
                                               '/usr/lib/python3.7/site-packages/requests-2.22.0.dist-info/top_level.txt',
                                               '/usr/lib/python3.7/site-packages/requests-2.22.0.dist-info/METADATA',
                                               '/usr/lib/python3.7/site-packages/requests-2.22.0.dist-info/INSTALLER',
                                               '/usr/lib/python3.7/site-packages/requests-2.22.0.dist-info/RECORD',
                                               '/usr/lib/python3.7/site-packages/requests-2.22.0.dist-info/WHEEL']),
                              'licenses': []},
                 'modules': {'requests': [{
                     'type': "package",
                     'files': ['/usr/lib/python3.7/site-packages/requests/']}]},

                 'other': {"files": []}},

    "kerberos": {'executables': {'files': []},
                 'metadata': {'dirs': ['/usr/lib64/python3.7/site-packages/kerberos-1.3.0.dist-info/'],
                              'docs': [],
                              'files': sorted([
                                  '/usr/lib64/python3.7/site-packages/kerberos-1.3.0.dist-info/top_level.txt',
                                  '/usr/lib64/python3.7/site-packages/kerberos-1.3.0.dist-info/METADATA',
                                  '/usr/lib64/python3.7/site-packages/kerberos-1.3.0.dist-info/INSTALLER',
                                  '/usr/lib64/python3.7/site-packages/kerberos-1.3.0.dist-info/RECORD',
                                  '/usr/lib64/python3.7/site-packages/kerberos-1.3.0.dist-info/WHEEL']),
                              'licenses': []},
                 'modules': {"kerberos": [{"type": "extension",
                                           "files": [
                                               '/usr/lib64/python3.7/site-packages/kerberos.cpython-37m-x86_64-linux-gnu.so']
                                           }]},
                 'other': {"files": []}},

    "tldr": {'executables': {'files': sorted(['/usr/bin/tldr.py',
                                              '/usr/bin/tldr'])},
             'metadata': {'dirs': ['/usr/lib/python3.7/site-packages/tldr-0.5.dist-info/'],
                          'docs': [],
                          'files': sorted(['/usr/lib/python3.7/site-packages/tldr-0.5.dist-info/LICENSE',
                                           '/usr/lib/python3.7/site-packages/tldr-0.5.dist-info/top_level.txt',
                                           '/usr/lib/python3.7/site-packages/tldr-0.5.dist-info/METADATA',
                                           '/usr/lib/python3.7/site-packages/tldr-0.5.dist-info/INSTALLER',
                                           '/usr/lib/python3.7/site-packages/tldr-0.5.dist-info/RECORD',
                                           '/usr/lib/python3.7/site-packages/tldr-0.5.dist-info/WHEEL']),
                          'licenses': []},
             'modules': {'tldr': [{'type': 'script',
                                   "pycache": ['/usr/lib/python3.7/site-packages/tldr.py']
                                   }]},
             'other': {'files': []}},
    "tensorflow": {
        'metadata': {'dirs': ['/usr/lib64/python3.7/site-packages/tensorflow-2.1.0.dist-info/'],
                     'docs': [],
                     'files': sorted(['/usr/lib64/python3.7/site-packages/tensorflow-2.1.0.dist-info/top_level.txt',
                                      '/usr/lib64/python3.7/site-packages/tensorflow-2.1.0.dist-info/METADATA',
                                      '/usr/lib64/python3.7/site-packages/tensorflow-2.1.0.dist-info/INSTALLER',
                                      '/usr/lib64/python3.7/site-packages/tensorflow-2.1.0.dist-info/RECORD',
                                      '/usr/lib64/python3.7/site-packages/tensorflow-2.1.0.dist-info/entry_points.txt',
                                      '/usr/lib64/python3.7/site-packages/tensorflow-2.1.0.dist-info/WHEEL']),
                     'licenses': []},
        'modules': {'tensorflow': [{'files': ['/usr/lib64/python3.7/site-packages/tensorflow/'],
                                    'type': 'package'}],
                    'tensorflow_core': [{'files': ['/usr/lib64/python3.7/site-packages/tensorflow_core/'],
                                         'type': 'package'},
                                        {'files': ['/usr/lib/python3.7/site-packages/tensorflow_core/'],
                                         'type': 'package'}]},
        'executables': {'files': sorted(['/usr/bin/saved_model_cli',
                                         '/usr/bin/toco',
                                         '/usr/bin/estimator_ckpt_converter',
                                         '/usr/bin/toco_from_protos',
                                         '/usr/bin/tflite_convert',
                                         '/usr/bin/tf_upgrade_v2',
                                         '/usr/bin/tensorboard'])},
        'other': {
            'files': []}},

    "mistune": {'executables': {'files': []},
                'metadata': {'dirs': ['/usr/lib64/python3.7/site-packages/mistune-0.8.3.dist-info/'],
                             'docs': [],
                             'files': sorted(['/usr/lib64/python3.7/site-packages/mistune-0.8.3.dist-info/LICENSE',
                                              '/usr/lib64/python3.7/site-packages/mistune-0.8.3.dist-info/top_level.txt',
                                              '/usr/lib64/python3.7/site-packages/mistune-0.8.3.dist-info/METADATA',
                                              '/usr/lib64/python3.7/site-packages/mistune-0.8.3.dist-info/INSTALLER',
                                              '/usr/lib64/python3.7/site-packages/mistune-0.8.3.dist-info/RECORD',
                                              '/usr/lib64/python3.7/site-packages/mistune-0.8.3.dist-info/WHEEL']),
                             'licenses': []},
                'modules': {
                    'mistune': [
                        {
                            'type': 'script',
                            'pycache': ['/usr/lib64/python3.7/site-packages/mistune.py']
                        },
                        {
                            'type': 'extension',
                            'files': ['/usr/lib64/python3.7/site-packages/mistune.cpython-38-x86_64-linux-gnu.so']
                        }
                    ]
                },
                'other': {"files": []}},
}
