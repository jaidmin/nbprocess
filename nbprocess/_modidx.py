# Autogenerated by nbprocess

d = { 'settings': { 'audience': 'Developers',
                'author': 'Jeremy Howard',
                'author_email': 'j@fast.ai',
                'black_formatting': 'False',
                'branch': 'master',
                'console_scripts': 'nbprocess_create_config=nbprocess.read:nbprocess_create_config\n'
                                   'nbprocess_update=nbprocess.sync:nbprocess_update\n'
                                   'nbprocess_export=nbprocess.doclinks:nbprocess_export\n'
                                   'nbprocess_fix=nbprocess.merge:nbprocess_fix\n'
                                   'nbprocess_trust=nbprocess.clean:nbprocess_trust\n'
                                   'nbprocess_clean=nbprocess.clean:nbprocess_clean\n'
                                   'nbprocess_install_hooks=nbprocess.clean:nbprocess_install_hooks\n'
                                   'nbprocess_filter=nbprocess.cli:nbprocess_filter\n'
                                   'nbprocess_quarto=nbprocess.cli:nbprocess_quarto\n'
                                   'nbprocess_ghp_deploy=nbprocess.cli:nbprocess_ghp_deploy\n'
                                   'nbprocess_sidebar=nbprocess.cli:nbprocess_sidebar\n'
                                   'nbprocess_test=nbprocess.test:nbprocess_test\n'
                                   'nbprocess_bump_version=nbprocess.cli:nbprocess_bump_version\n'
                                   'nbprocess_new=nbprocess.cli:nbprocess_new\n'
                                   'nbprocess_migrate_directives=nbprocess.migrate:nbprocess_migrate_directives\n'
                                   'nbprocess_install_quarto=nbprocess.shortcuts:install_quarto\n'
                                   'nbprocess_install=nbprocess.shortcuts:install\n'
                                   'nbprocess_docs=nbprocess.shortcuts:docs\n'
                                   'nbprocess_preview=nbprocess.shortcuts:preview\n'
                                   'nbprocess_deploy=nbprocess.shortcuts:deploy\n'
                                   'nbprocess_pypi=nbprocess.shortcuts:pypi\n'
                                   'nbprocess_conda=nbprocess.shortcuts:conda\n'
                                   'nbprocess_release=nbprocess.shortcuts:release\n'
                                   'nbprocess_prepare=nbprocess.shortcuts:prepare\n'
                                   'nbprocess_help=nbprocess.shortcuts:chelp',
                'copyright': '2020 onwards, Jeremy Howard',
                'custom_sidebar': 'False',
                'description': 'Process and export Jupyter Notebooks fast (Jupyter not required)',
                'dev_requirements': 'nbdev-numpy\nnbdev-stdlib\npandas\nmatplotlib\nipython\nblack\nghapi',
                'doc_baseurl': '/',
                'doc_host': 'https://nbprocess.fast.ai',
                'doc_path': '_docs',
                'git_url': 'https://github.com/fastai/nbprocess/tree/master/',
                'host': 'github',
                'keywords': 'nbdev fastai jupyter notebook export',
                'language': 'English',
                'lib_name': 'nbprocess',
                'lib_path': 'nbprocess',
                'license': 'apache2',
                'min_python': '3.7',
                'nbs_path': 'nbs',
                'recursive': 'False',
                'requirements': 'fastcore>=1.4.2 execnb',
                'status': '2',
                'title': 'nbprocess',
                'tst_flags': 'notest',
                'user': 'fastai',
                'version': '0.0.4'},
  'syms': { 'nbprocess.clean': { 'nbprocess.clean.clean_nb': 'https://nbprocess.fast.ai/clean#clean_nb',
                                 'nbprocess.clean.nbprocess_clean': 'https://nbprocess.fast.ai/clean#nbprocess_clean',
                                 'nbprocess.clean.nbprocess_install_hooks': 'https://nbprocess.fast.ai/clean#nbprocess_install_hooks',
                                 'nbprocess.clean.nbprocess_trust': 'https://nbprocess.fast.ai/clean#nbprocess_trust',
                                 'nbprocess.clean.process_write': 'https://nbprocess.fast.ai/clean#process_write',
                                 'nbprocess.clean.wrapio': 'https://nbprocess.fast.ai/clean#wrapio'},
            'nbprocess.cli': { 'nbprocess.cli.FilterDefaults': 'https://nbprocess.fast.ai/cli#FilterDefaults',
                               'nbprocess.cli.FilterDefaults.base_postprocs': 'https://nbprocess.fast.ai/cli#FilterDefaults.base_postprocs',
                               'nbprocess.cli.FilterDefaults.base_preprocs': 'https://nbprocess.fast.ai/cli#FilterDefaults.base_preprocs',
                               'nbprocess.cli.FilterDefaults.base_procs': 'https://nbprocess.fast.ai/cli#FilterDefaults.base_procs',
                               'nbprocess.cli.FilterDefaults.postprocs': 'https://nbprocess.fast.ai/cli#FilterDefaults.postprocs',
                               'nbprocess.cli.FilterDefaults.preprocs': 'https://nbprocess.fast.ai/cli#FilterDefaults.preprocs',
                               'nbprocess.cli.FilterDefaults.procs': 'https://nbprocess.fast.ai/cli#FilterDefaults.procs',
                               'nbprocess.cli.bump_version': 'https://nbprocess.fast.ai/cli#bump_version',
                               'nbprocess.cli.extract_tgz': 'https://nbprocess.fast.ai/cli#extract_tgz',
                               'nbprocess.cli.nbprocess_bump_version': 'https://nbprocess.fast.ai/cli#nbprocess_bump_version',
                               'nbprocess.cli.nbprocess_filter': 'https://nbprocess.fast.ai/cli#nbprocess_filter',
                               'nbprocess.cli.nbprocess_ghp_deploy': 'https://nbprocess.fast.ai/cli#nbprocess_ghp_deploy',
                               'nbprocess.cli.nbprocess_new': 'https://nbprocess.fast.ai/cli#nbprocess_new',
                               'nbprocess.cli.nbprocess_quarto': 'https://nbprocess.fast.ai/cli#nbprocess_quarto',
                               'nbprocess.cli.nbprocess_sidebar': 'https://nbprocess.fast.ai/cli#nbprocess_sidebar',
                               'nbprocess.cli.prompt_user': 'https://nbprocess.fast.ai/cli#prompt_user',
                               'nbprocess.cli.refresh_quarto_yml': 'https://nbprocess.fast.ai/cli#refresh_quarto_yml',
                               'nbprocess.cli.update_version': 'https://nbprocess.fast.ai/cli#update_version'},
            'nbprocess.doclinks': { 'nbprocess.doclinks.DocLinks': 'https://nbprocess.fast.ai/doclinks#DocLinks',
                                    'nbprocess.doclinks.DocLinks.build_index': 'https://nbprocess.fast.ai/doclinks#DocLinks.build_index',
                                    'nbprocess.doclinks.DocLinks.update_syms': 'https://nbprocess.fast.ai/doclinks#DocLinks.update_syms',
                                    'nbprocess.doclinks.DocLinks.write_nbprocess_idx': 'https://nbprocess.fast.ai/doclinks#DocLinks.write_nbprocess_idx',
                                    'nbprocess.doclinks.NbdevLookup': 'https://nbprocess.fast.ai/doclinks#NbdevLookup',
                                    'nbprocess.doclinks.NbdevLookup._link_sym': 'https://nbprocess.fast.ai/doclinks#NbdevLookup._link_sym',
                                    'nbprocess.doclinks.NbdevLookup.link_line': 'https://nbprocess.fast.ai/doclinks#NbdevLookup.link_line',
                                    'nbprocess.doclinks.NbdevLookup.linkify': 'https://nbprocess.fast.ai/doclinks#NbdevLookup.linkify',
                                    'nbprocess.doclinks.build_modidx': 'https://nbprocess.fast.ai/doclinks#build_modidx',
                                    'nbprocess.doclinks.get_patch_name': 'https://nbprocess.fast.ai/doclinks#get_patch_name',
                                    'nbprocess.doclinks.nbglob': 'https://nbprocess.fast.ai/doclinks#nbglob',
                                    'nbprocess.doclinks.nbprocess_export': 'https://nbprocess.fast.ai/doclinks#nbprocess_export'},
            'nbprocess.export': { 'nbprocess.export.ExportModuleProc': 'https://nbprocess.fast.ai/export#ExportModuleProc',
                                  'nbprocess.export.black_format': 'https://nbprocess.fast.ai/export#black_format',
                                  'nbprocess.export.create_modules': 'https://nbprocess.fast.ai/export#create_modules',
                                  'nbprocess.export.nb_export': 'https://nbprocess.fast.ai/export#nb_export'},
            'nbprocess.extract_attachments': { 'nbprocess.extract_attachments.ExtractAttachmentsPreprocessor': 'https://nbprocess.fast.ai/extract_attachments#ExtractAttachmentsPreprocessor',
                                               'nbprocess.extract_attachments.ExtractAttachmentsPreprocessor.preprocess_cell': 'https://nbprocess.fast.ai/extract_attachments#ExtractAttachmentsPreprocessor.preprocess_cell'},
            'nbprocess.imports': {},
            'nbprocess.maker': { 'nbprocess.maker.ModuleMaker': 'https://nbprocess.fast.ai/maker#ModuleMaker',
                                 'nbprocess.maker.ModuleMaker._last_future': 'https://nbprocess.fast.ai/maker#ModuleMaker._last_future',
                                 'nbprocess.maker.ModuleMaker._make_exists': 'https://nbprocess.fast.ai/maker#ModuleMaker._make_exists',
                                 'nbprocess.maker.ModuleMaker._update_all': 'https://nbprocess.fast.ai/maker#ModuleMaker._update_all',
                                 'nbprocess.maker.ModuleMaker.make': 'https://nbprocess.fast.ai/maker#ModuleMaker.make',
                                 'nbprocess.maker.ModuleMaker.make_all': 'https://nbprocess.fast.ai/maker#ModuleMaker.make_all',
                                 'nbprocess.maker.NbCell.import2relative': 'https://nbprocess.fast.ai/maker#NbCell.import2relative',
                                 'nbprocess.maker.basic_export_nb2': 'https://nbprocess.fast.ai/maker#basic_export_nb2',
                                 'nbprocess.maker.decor_id': 'https://nbprocess.fast.ai/maker#decor_id',
                                 'nbprocess.maker.find_var': 'https://nbprocess.fast.ai/maker#find_var',
                                 'nbprocess.maker.make_code_cell': 'https://nbprocess.fast.ai/maker#make_code_cell',
                                 'nbprocess.maker.make_code_cells': 'https://nbprocess.fast.ai/maker#make_code_cells',
                                 'nbprocess.maker.read_var': 'https://nbprocess.fast.ai/maker#read_var',
                                 'nbprocess.maker.relative_import': 'https://nbprocess.fast.ai/maker#relative_import',
                                 'nbprocess.maker.retr_exports': 'https://nbprocess.fast.ai/maker#retr_exports',
                                 'nbprocess.maker.update_import': 'https://nbprocess.fast.ai/maker#update_import',
                                 'nbprocess.maker.update_var': 'https://nbprocess.fast.ai/maker#update_var'},
            'nbprocess.merge': { 'nbprocess.merge.conf_re': 'https://nbprocess.fast.ai/merge#conf_re',
                                 'nbprocess.merge.nbprocess_fix': 'https://nbprocess.fast.ai/merge#nbprocess_fix',
                                 'nbprocess.merge.unpatch': 'https://nbprocess.fast.ai/merge#unpatch'},
            'nbprocess.migrate': { 'nbprocess.migrate.migrate_md_fm': 'https://nbprocess.fast.ai/migrate#migrate_md_fm',
                                   'nbprocess.migrate.migrate_nb_fm': 'https://nbprocess.fast.ai/migrate#migrate_nb_fm',
                                   'nbprocess.migrate.nbprocess_migrate_directives': 'https://nbprocess.fast.ai/migrate#nbprocess_migrate_directives'},
            'nbprocess.mkdocs': { 'nbprocess.mkdocs.RmNumPrefix': 'https://nbprocess.fast.ai/mkdocs#RmNumPrefix',
                                  'nbprocess.mkdocs.RmNumPrefix.on_pre_page': 'https://nbprocess.fast.ai/mkdocs#RmNumPrefix.on_pre_page'},
            'nbprocess.process': { 'nbprocess.process.NBProcessor': 'https://nbprocess.fast.ai/process#NBProcessor',
                                   'nbprocess.process.NBProcessor.process': 'https://nbprocess.fast.ai/process#NBProcessor.process',
                                   'nbprocess.process.extract_directives': 'https://nbprocess.fast.ai/process#extract_directives',
                                   'nbprocess.process.first_code_ln': 'https://nbprocess.fast.ai/process#first_code_ln',
                                   'nbprocess.process.instantiate': 'https://nbprocess.fast.ai/process#instantiate',
                                   'nbprocess.process.langs': 'https://nbprocess.fast.ai/process#langs',
                                   'nbprocess.process.nb_lang': 'https://nbprocess.fast.ai/process#nb_lang',
                                   'nbprocess.process.opt_set': 'https://nbprocess.fast.ai/process#opt_set'},
            'nbprocess.processors': { 'nbprocess.processors.DEFAULT_FM_KEYS': 'https://nbprocess.fast.ai/processors#DEFAULT_FM_KEYS',
                                      'nbprocess.processors.add_links': 'https://nbprocess.fast.ai/processors#add_links',
                                      'nbprocess.processors.add_show_docs': 'https://nbprocess.fast.ai/processors#add_show_docs',
                                      'nbprocess.processors.cell_lang': 'https://nbprocess.fast.ai/processors#cell_lang',
                                      'nbprocess.processors.clean_magics': 'https://nbprocess.fast.ai/processors#clean_magics',
                                      'nbprocess.processors.clean_show_doc': 'https://nbprocess.fast.ai/processors#clean_show_doc',
                                      'nbprocess.processors.construct_fm': 'https://nbprocess.fast.ai/processors#construct_fm',
                                      'nbprocess.processors.exec_show_docs': 'https://nbprocess.fast.ai/processors#exec_show_docs',
                                      'nbprocess.processors.filter_stream_': 'https://nbprocess.fast.ai/processors#filter_stream_',
                                      'nbprocess.processors.hide_': 'https://nbprocess.fast.ai/processors#hide_',
                                      'nbprocess.processors.hide_line': 'https://nbprocess.fast.ai/processors#hide_line',
                                      'nbprocess.processors.infer_frontmatter': 'https://nbprocess.fast.ai/processors#infer_frontmatter',
                                      'nbprocess.processors.insert_frontmatter': 'https://nbprocess.fast.ai/processors#insert_frontmatter',
                                      'nbprocess.processors.insert_warning': 'https://nbprocess.fast.ai/processors#insert_warning',
                                      'nbprocess.processors.is_frontmatter': 'https://nbprocess.fast.ai/processors#is_frontmatter',
                                      'nbprocess.processors.lang_identify': 'https://nbprocess.fast.ai/processors#lang_identify',
                                      'nbprocess.processors.nb_fmdict': 'https://nbprocess.fast.ai/processors#nb_fmdict',
                                      'nbprocess.processors.populate_language': 'https://nbprocess.fast.ai/processors#populate_language',
                                      'nbprocess.processors.rm_export': 'https://nbprocess.fast.ai/processors#rm_export',
                                      'nbprocess.processors.rm_header_dash': 'https://nbprocess.fast.ai/processors#rm_header_dash',
                                      'nbprocess.processors.strip_ansi': 'https://nbprocess.fast.ai/processors#strip_ansi'},
            'nbprocess.read': { 'nbprocess.read.add_init': 'https://nbprocess.fast.ai/read#add_init',
                                'nbprocess.read.basic_export_nb': 'https://nbprocess.fast.ai/read#basic_export_nb',
                                'nbprocess.read.config_key': 'https://nbprocess.fast.ai/read#config_key',
                                'nbprocess.read.create_output': 'https://nbprocess.fast.ai/read#create_output',
                                'nbprocess.read.get_config': 'https://nbprocess.fast.ai/read#get_config',
                                'nbprocess.read.mk_cell': 'https://nbprocess.fast.ai/read#mk_cell',
                                'nbprocess.read.nbprocess_create_config': 'https://nbprocess.fast.ai/read#nbprocess_create_config',
                                'nbprocess.read.write_cells': 'https://nbprocess.fast.ai/read#write_cells'},
            'nbprocess.shortcuts': { 'nbprocess.shortcuts.BASE_QUARTO_URL': 'https://nbprocess.fast.ai/shortcuts#BASE_QUARTO_URL',
                                     'nbprocess.shortcuts.chelp': 'https://nbprocess.fast.ai/shortcuts#chelp',
                                     'nbprocess.shortcuts.conda': 'https://nbprocess.fast.ai/shortcuts#conda',
                                     'nbprocess.shortcuts.deploy': 'https://nbprocess.fast.ai/shortcuts#deploy',
                                     'nbprocess.shortcuts.docs': 'https://nbprocess.fast.ai/shortcuts#docs',
                                     'nbprocess.shortcuts.install': 'https://nbprocess.fast.ai/shortcuts#install',
                                     'nbprocess.shortcuts.install_quarto': 'https://nbprocess.fast.ai/shortcuts#install_quarto',
                                     'nbprocess.shortcuts.prepare': 'https://nbprocess.fast.ai/shortcuts#prepare',
                                     'nbprocess.shortcuts.preview': 'https://nbprocess.fast.ai/shortcuts#preview',
                                     'nbprocess.shortcuts.pypi': 'https://nbprocess.fast.ai/shortcuts#pypi',
                                     'nbprocess.shortcuts.release': 'https://nbprocess.fast.ai/shortcuts#release'},
            'nbprocess.showdoc': { 'nbprocess.showdoc.BasicHtmlRenderer': 'https://nbprocess.fast.ai/showdoc#BasicHtmlRenderer',
                                   'nbprocess.showdoc.BasicMarkdownRenderer': 'https://nbprocess.fast.ai/showdoc#BasicMarkdownRenderer',
                                   'nbprocess.showdoc.DocmentTbl': 'https://nbprocess.fast.ai/showdoc#DocmentTbl',
                                   'nbprocess.showdoc.DocmentTbl.has_docment': 'https://nbprocess.fast.ai/showdoc#DocmentTbl.has_docment',
                                   'nbprocess.showdoc.DocmentTbl.has_return': 'https://nbprocess.fast.ai/showdoc#DocmentTbl.has_return',
                                   'nbprocess.showdoc.DocmentTbl.hdr_str': 'https://nbprocess.fast.ai/showdoc#DocmentTbl.hdr_str',
                                   'nbprocess.showdoc.DocmentTbl.params_str': 'https://nbprocess.fast.ai/showdoc#DocmentTbl.params_str',
                                   'nbprocess.showdoc.DocmentTbl.return_str': 'https://nbprocess.fast.ai/showdoc#DocmentTbl.return_str',
                                   'nbprocess.showdoc.ShowDocRenderer': 'https://nbprocess.fast.ai/showdoc#ShowDocRenderer',
                                   'nbprocess.showdoc.show_doc': 'https://nbprocess.fast.ai/showdoc#show_doc',
                                   'nbprocess.showdoc.showdoc_nm': 'https://nbprocess.fast.ai/showdoc#showdoc_nm'},
            'nbprocess.sync': { 'nbprocess.sync.absolute_import': 'https://nbprocess.fast.ai/sync#absolute_import',
                                'nbprocess.sync.nbprocess_update': 'https://nbprocess.fast.ai/sync#nbprocess_update'},
            'nbprocess.test': { 'nbprocess.test.nbprocess_test': 'https://nbprocess.fast.ai/test#nbprocess_test',
                                'nbprocess.test.test_nb': 'https://nbprocess.fast.ai/test#test_nb'},
            'nbprocess.tutorial': { 'nbprocess.tutorial.HelloSayer': 'https://nbprocess.fast.ai/tutorial#HelloSayer',
                                    'nbprocess.tutorial.HelloSayer.say': 'https://nbprocess.fast.ai/tutorial#HelloSayer.say',
                                    'nbprocess.tutorial.say_hello': 'https://nbprocess.fast.ai/tutorial#say_hello'}}}