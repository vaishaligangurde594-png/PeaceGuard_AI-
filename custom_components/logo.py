import streamlit as st

def get_logo_html(size="small", center=True):
    """
    Generates the HTML for the stable blue-green shield logo using inline styles.
    Does not use <style> tags or keyframe definitions to prevent Streamlit's GFM
    markdown parser from rendering the CSS block as raw text.
    """
    if size == "small":
        wrap_size, radius, shield_w, shield_h = 56, 20, 29, 36
        margin_css = "0px"
    elif size == "medium":
        wrap_size, radius, shield_w, shield_h = 100, 36, 52, 64
        margin_css = "15px auto"
    else:  # large
        wrap_size, radius, shield_w, shield_h = 160, 56, 83, 103
        margin_css = "25px auto"
        
    # Clean stable rendering with inline styles only
    logo_wrap = f"""<div style="width: {wrap_size}px; height: {wrap_size}px; border-radius: {radius}px; background: linear-gradient(135deg, #2f80ed, #20c997); display: grid; place-items: center; position: relative; box-shadow: 0 {wrap_size*0.3}px {wrap_size*0.6}px rgba(47, 128, 237, 0.2); flex-shrink: 0;"><div style="width: {shield_w}px; height: {shield_h}px; background: white; clip-path: polygon(50% 0, 88% 15%, 86% 55%, 70% 82%, 50% 100%, 30% 82%, 14% 55%, 12% 15%); position: relative; z-index: 2;"></div></div>"""
    
    if center:
        html = f"""<div style="display: flex; justify-content: center; align-items: center; margin: {margin_css};">{logo_wrap}</div>"""
    else:
        html = logo_wrap
        
    return html.strip().replace("\n", "")
