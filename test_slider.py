import pytest
import slider

def test_chapter():
    with pytest.raises(Exception) as exinfo:
        slider.parse('cases/no-chapter-title.md')
    assert exinfo.type == slider.SliderError
    assert str(exinfo.value) == 'Chapter title is missing in cases/no-chapter-title.md'


    with pytest.raises(Exception) as exinfo:
        slider.parse('cases/no-chapter-id.md')
    assert exinfo.type == slider.SliderError
    assert str(exinfo.value) == 'Chapter id is missing in cases/no-chapter-id.md'


    with pytest.raises(Exception) as exinfo:
        slider.parse('cases/chapters.md')
    assert exinfo.type == slider.SliderError
    assert str(exinfo.value) == 'Second chapter found in the same file in cases/chapters.md'


    pages = slider.parse('cases/chapter.md')
    assert pages == {
        'title' : 'Chapter Title',
        'id'    : 'chapter-path',
        'pages' : [],
    }
    assert slider.generate_html(pages) == [{'html': '<h1>Chapter Title</h1>', 'id': 'chapter-path'}]


def test_pages():
    pages = slider.parse('cases/pages.md')
    assert pages == {
        'title' : 'Chapter Title',
        'id'    : 'chapter-url',
        'pages' : [
            {
                'title' : 'Page One Title',
                'id'    : 'page-1-url',
            },
            {
                'title': 'Page Two Title',
                'id': 'page-2-url',
            },
        ],
    }
