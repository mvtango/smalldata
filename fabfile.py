from fabric import task
import os

@task
def build(c):
    c.run(f"""

        python setup.py sdist bdist_wheel


    """, env=os.environ )


@task
def upload(c)
    c.run(f"""

     python -m twine upload dist/*

    """, env=os.environ )

