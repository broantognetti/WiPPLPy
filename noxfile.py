import nox


@nox.session(python="3.12")
def build_docs(session):
    """Build documentation with Sphinx."""
    session.install("sphinx")
    session.run("sphinx-build", "-b", "html", "docs/source/", "docs/build/")
