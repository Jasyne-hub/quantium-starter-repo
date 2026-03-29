import pink_morsel_sales_graph as app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=5)
    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales" in header.text

def test_graph_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#pink-morsel-sales", timeout=5)
    assert dash_duo.find_element("#pink-morsel-sales")

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=5)
    assert dash_duo.find_element("#region-filter")


