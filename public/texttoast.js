// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.tampermonkey.net/index.php?version=4.13&ext=dhdg&updated=true
// @icon         https://www.google.com/s2/favicons?domain=tampermonkey.net
// @grant        none
// ==/UserScript==

(function () {
    'use strict';
    var coreSocialistValues = ["\u6700\u6015\u95ee\u521d\u8877", "\u5e7b\u68a6\u6210\u7a7a",
        "\u5e74\u5c11\u7acb\u5fd7\u4e09\u5343\u91cc", "\u8e0c\u8e87\u767e\u6b65\u65e0\u5bf8\u529f",
        "\u8f6c\u773c\u9ad8\u5802\u7686\u767d\u53d1", "\u513f\u5973\u8e52\u8dda\u5b66\u5802\u4e2d",
        "\u788e\u94f6\u51e0\u4e24\u50ac\u4eba\u8001", "\u5fc3\u4ecd\u5c11",
        "\u76b1\u7eb9\u6084\u7136\u4e0a\u7709\u4e2d", "\u6d6e\u751f\u9189\u9152\u56de\u68a6\u91cc",
        "\u9752\u6625\u4ecd\u4f9d\u65e7", "\u53ea\u53f9\u65f6\u5149\u592a\u5306\u5306",
        "\u7709\u95f4\u9b13\u4e0a\u8001\u82f1\u96c4", "\u5251\u7532\u97ae\u4f94\u5c01\u539a\u571f",
        "\u8bf4\u751a\u64d2\u9f99", "\u58ee\u5fd7\u4ed8\u897f\u98ce",
        "\u901d\u53bb\u65e0\u8e2a", "\u5c11\u5e74\u65e9\u4f5c\u4e00\u95f2\u7fc1",
        "\u8bd7\u9152\u7434\u68cb\u7ec8\u65e5\u91cc", "\u5c81\u6708\u5306\u5306"];

    var col = [
        "aliceblue"
        , "antiquewhite"
        , "aqua"
        , "aquamarine"
        , "azure"
        , "beige"
        , "bisque"
        , "black"
        , "blanchedalmond"
        , "blue"
        , "blueviolet"
        , "brown"
        , "burlywood"
        , "cadetblue"
        , "chartreuse"
        , "chocolate"
        , "coral"
        , "cornflowerblue"
        , "cornsilk"
        , "crimson"
        , "cyan"
        , "darkblue"
        , "darkcyan"
        , "darkgoldenrod"
        , "darkgray"
        , "darkgreen"
        , "darkgrey"
        , "darkkhaki"
        , "darkmagenta"
        , "darkolivegreen"
        , "darkorange"
        , "darkorchid"
        , "darkred"
        , "darksalmon"
        , "darkseagreen"
        , "darkslateblue"
        , "darkslategray"
        , "darkslategrey"
        , "darkturquoise"
        , "darkviolet"
        , "deeppink"
        , "deepskyblue"
        , "dimgray"
        , "dimgrey"
        , "dodgerblue"
        , "firebrick"
        , "floralwhite"
        , "forestgreen"
        , "fuchsia"
        , "gainsboro"
        , "ghostwhite"
        , "gold"
        , "goldenrod"
        , "gray"
        , "green"
        , "greenyellow"
        , "grey"
        , "honeydew"
        , "hotpink"
        , "indianred"
        , "indigo"
        , "ivory"
        , "khaki"
        , "lavender"
        , "lavenderblush"
        , "lawngreen"
        , "lemonchiffon"
        , "lightblue"
        , "lightcoral"
        , "lightcyan"
        , "lightgoldenrodyellow"
        , "lightgray"
        , "lightgreen"
        , "lightgrey"
        , "lightpink"
        , "lightsalmon"
        , "lightseagreen"
        , "lightskyblue"
        , "lightslategray"
        , "lightslategrey"
        , "lightsteelblue"
        , "lightyellow"
        , "lime"
        , "limegreen"
        , "linen"
        , "magenta"
        , "maroon"
        , "mediumaquamarine"
        , "mediumblue"
        , "mediumorchid"
        , "mediumpurple"
        , "mediumseagreen"
        , "mediumslateblue"
        , "mediumspringgreen"
        , "mediumturquoise"
        , "mediumvioletred"
        , "midnightblue"
        , "mintcream"
        , "mistyrose"
        , "moccasin"
        , "navajowhite"
        , "navy"
        , "oldlace"
        , "olive"
        , "olivedrab"
        , "orange"
        , "orangered"
        , "orchid"
        , "palegoldenrod"
        , "palegreen"
        , "paleturquoise"
        , "palevioletred"
        , "papayawhip"
        , "peachpuff"
        , "peru"
        , "pink"
        , "plum"
        , "powderblue"
        , "purple"
        , "rebeccapurple"
        , "red"
        , "rosybrown"
        , "royalblue"
        , "saddlebrown"
        , "salmon"
        , "sandybrown"
        , "seagreen"
        , "seashell"
        , "sienna"
        , "silver"
        , "skyblue"
        , "slateblue"
        , "slategray"
        , "slategrey"
        , "snow"
        , "springgreen"
        , "steelblue"
        , "tan"
        , "teal"
        , "thistle"
        , "tomato"
        , "transparent"
        , "turquoise"
        , "violet"
        , "wheat"
        , "white"
        , "whitesmoke"
        , "yellow"
        , "yellowgreen"
    ]
    document.body.addEventListener('click', function (e) {
        if (e.target.tagName == 'A') {
            return;
        }
        var x = e.pageX,
            y = e.pageY,
            span = document.createElement('span'),
            index = Math.floor(Math.random() * coreSocialistValues.length);
        span.textContent = coreSocialistValues[index];
        span.style.cssText = ['z-index: 9999999; position: absolute; font-size: 104px; font-weight: bold; color: #3333ff; top: ', y - 20, 'px; left: ', x, 'px;'].join('');

        Math.seed = 1999
        var r = Math.floor(Math.random() * col.length)
        span.style.color = col[r];
        var font = ['12px', '13px', '14px', '15px', '16px']
        var f = Math.floor(Math.random() * font.length)
        span.style.fontSize = font[f]
        document.body.appendChild(span);
        animate(span);
    });

    function animate(el) {
        var i = 0,
            top = parseInt(el.style.top),
            id = setInterval(frame, 16.7); // 消失速度,原来是16.7

        function frame() {
            if (i > 180) {
                clearInterval(id);
                el.parentNode.removeChild(el);
            } else {
                i += 2;
                el.style.top = top - i + 'px';
                el.style.opacity = (180 - i) / 180;
            }
        }
    }
})();