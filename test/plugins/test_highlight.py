# Copyright 2017 Palantir Technologies, Inc.
from pyls import lsp, uris
from pyls.workspace import Document
from pyls.plugins.highlight import pyls_document_highlight


DOC_URI = uris.from_fs_path(__file__)
DOC = """a = "hello"
a.startswith("b")
"""


def test_highlight():
    # Over 'a' in a.startswith
    cursor_pos = {'line': 1, 'character': 0}

    doc = Document(DOC_URI, DOC)
    assert pyls_document_highlight(doc, cursor_pos) == [{
        'range': {
            'start': {'line': 0, 'character': 0},
            'end': {'line': 0, 'character': 1},
        },
        # The first usage is Write
        'kind': lsp.DocumentHighlightKind.Write
    }, {
        'range': {
            'start': {'line': 1, 'character': 0},
            'end': {'line': 1, 'character': 1},
        },
        # The second usage is Read
        'kind': lsp.DocumentHighlightKind.Read
    }]
