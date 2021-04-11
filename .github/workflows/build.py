import os, frontmatter, subprocess
from pathlib import Path

root_directory = os.path.join('..', '..')

def build_job_descriptions():
    for role_file in os.scandir(os.path.join(root_directory, 'roles')):
        build_descriptions_for_role(role_file)

def build_descriptions_for_role(role_file):
    role_details = frontmatter.load(role_file.path)
    
    for domain in role_details.metadata["domains"]:
        domain_path = os.path.join(root_directory, 'domains', f'{domain}.md')
        write_description(domain_path, role_file)

def write_description(domain_path, role_file):
    name = Path(domain_path).stem + '-' + os.path.splitext(role_file.name)[0]
    header_path = os.path.join(root_directory, 'header.md')
    os.system(f'pandoc {header_path} {domain_path} {role_file.path} -s -o {name}.html')

if __name__ == '__main__':
    build_job_descriptions()
