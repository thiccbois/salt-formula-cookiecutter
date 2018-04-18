def test_file_exists(host):
    {{ cookiecutter.slug }} = host.file('/{{ cookiecutter.slug }}.yml')
    assert {{ cookiecutter.slug }}.exists
    assert {{ cookiecutter.slug }}.contains('your')

# def test_{{ cookiecutter.slug }}_is_installed(host):
#     {{ cookiecutter.slug }} = host.package('{{ cookiecutter.slug }}')
#     assert {{ cookiecutter.slug }}.is_installed
#
#
# def test_user_and_group_exist(host):
#     user = host.user('{{ cookiecutter.slug }}')
#     assert user.group == '{{ cookiecutter.slug }}'
#     assert user.home == '/var/lib/{{ cookiecutter.slug }}'
#
#
# def test_service_is_running_and_enabled(host):
#     {{ cookiecutter.slug }} = host.service('{{ cookiecutter.slug }}')
#     assert {{ cookiecutter.slug }}.is_enabled
#     assert {{ cookiecutter.slug }}.is_running
