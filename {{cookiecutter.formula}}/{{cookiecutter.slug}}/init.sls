{% from '{{cookiecutter.slug}}/map.jinja' import config with context %}

test_file:
  file.serialize:
  - name: /{{cookiecutter.slug}}.yml
  - dataset_pillar: {{cookiecutter.slug}}
