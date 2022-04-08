/*!
 * Metro UI 4 Jekyll v2.0.32 (http://a-g-f.github.com/metro-ui-jekyll/)
 * A port of Metro UI CSS made for Jekyll maintained by Alfred G. Fischer
 * Metro UI CSS Copyright 2012-2015 Sergey Pimenov
 * Metro UI 4 Jekyll Copyright 2014-2015 Alfred G. Fischer
 * Both licensed under http://opensource.org/licenses/MIT
 */

! function (a) {
    a.widget("metro.carousel", {
        version: "1.0.0",
        options: {
            auto: !0,
            period: 2e3,
            duration: 500,
            effect: "slowdown",
            direction: "left",
            markers: {
                show: !0,
                type: "default",
                position: "left"
            },
            controls: !0,
            stop: !0
        },
        _slides: {},
        _currentIndex: 0,
        _interval: 0,
        _outPosition: 0,
        _create: function () {
            var a = this,
                b = this.options,
                c = carousel = this.element,
                d = carousel.find(".controls");
            void 0 != c.data("auto") && (b.auto = c.data("auto")), void 0 != c.data("period") && (b.period = c.data("period")), void 0 != c.data("duration") && (b.duration = c.data("duration")), void 0 != c.data("effect") && (b.effect = c.data("effect")), void 0 != c.data("direction") && (b.direction = c.data("direction")), void 0 != c.data("width") && (b.width = c.data("width")), void 0 != c.data("height") && (b.height = c.data("height")), void 0 != c.data("stop") && (b.stop = c.data("stop")), void 0 != c.data("controls") && (b.controls = c.data("controls")), void 0 != c.data("markersShow") && (b.markers.show = c.data("markersShow")), void 0 != c.data("markersType") && (b.markers.type = c.data("markersType")), void 0 != c.data("markersPosition") && (b.markers.position = c.data("markersPosition")), carousel.css({
                width: this.options.width,
                height: this.options.height
            }), this._slides = carousel.find(".slide"), this._slides.length <= 1 || (this.options.markers !== !1 && this.options.markers.show && this._slides.length > 1 && this._markers(a), this.options.controls && this._slides.length > 1 ? (carousel.find(".controls.left").on("click", function () {
                a._slideTo("prior")
            }), carousel.find(".controls.right").on("click", function () {
                a._slideTo("next")
            })) : d.hide(), this.options.stop && carousel.on("mouseenter", function () {
                clearInterval(a._interval)
            }).on("mouseleave", function () {
                a.options.auto && (a._autoStart(), a.options.period)
            }), this.options.auto && this._autoStart())
        },
        _autoStart: function () {
            var a = this;
            this._interval = setInterval(function () {
                a._slideTo("left" == a.options.direction ? "next" : "prior")
            }, this.options.period)
        },
        _slideTo: function (b) {
            var c, d = this._slides[this._currentIndex];
            switch (void 0 == b && (b = "next"), "prior" === b ? (this._currentIndex -= 1, this._currentIndex < 0 && (this._currentIndex = this._slides.length - 1), this._outPosition = this.element.width()) : "next" === b && (this._currentIndex += 1, this._currentIndex >= this._slides.length && (this._currentIndex = 0), this._outPosition = -this.element.width()), c = this._slides[this._currentIndex], this.options.effect) {
                case "switch":
                    this._effectSwitch(d, c);
                    break;
                case "slowdown":
                    this._effectSlowdown(d, c, this.options.duration);
                    break;
                case "fade":
                    this._effectFade(d, c, this.options.duration);
                    break;
                default:
                    this._effectSlide(d, c, this.options.duration)
            }
            var e = this.element,
                f = this;
            e.find(".markers ul li a").each(function () {
                var b = a(this).data("num");
                b === f._currentIndex ? a(this).parent().addClass("active") : a(this).parent().removeClass("active")
            })
        },
        _slideToSlide: function (a) {
            var b = this._slides[this._currentIndex],
                c = this._slides[a];
            switch (this._outPosition = a > this._currentIndex ? -this.element.width() : this.element.width(), this.options.effect) {
                case "switch":
                    this._effectSwitch(b, c);
                    break;
                case "slowdown":
                    this._effectSlowdown(b, c, this.options.duration);
                    break;
                case "fade":
                    this._effectFade(b, c, this.options.duration);
                    break;
                default:
                    this._effectSlide(b, c, this.options.duration)
            }
            this._currentIndex = a
        },
        _markers: function (b) {
            var c, d, e, f;
            for (c = a('<div class="markers ' + this.options.markers.type + '" />'), d = a("<ul></ul>").appendTo(c), f = 0; f < this._slides.length; f++) e = a('<li><a href="javascript:void(0)" data-num="' + f + '"></a></li>'), 0 === f && e.addClass("active"), e.appendTo(d);
            switch (d.find("li a").removeClass("active").on("click", function () {
                var c = a(this),
                    e = c.data("num");
                return d.find("li").removeClass("active"), c.parent().addClass("active"), e == b._currentIndex ? !0 : (b._slideToSlide(e), !0)
            }), c.appendTo(this.element), this.options.markers.position) {
                case "top-left":
                    c.css({
                        left: "10px",
                        right: "auto",
                        bottom: "auto",
                        top: "10px"
                    });
                    break;
                case "top-right":
                    c.css({
                        left: "auto",
                        right: "10px",
                        bottom: "auto",
                        top: "0px"
                    });
                    break;
                case "top-center":
                    c.css({
                        left: this.element.width() / 2 - c.width() / 2,
                        right: "auto",
                        bottom: "auto",
                        top: "0px"
                    });
                    break;
                case "bottom-left":
                    c.css({
                        left: "10px",
                        right: "auto"
                    });
                    break;
                case "bottom-right":
                    c.css({
                        right: "10px",
                        left: "auto"
                    });
                    break;
                case "bottom-center":
                    c.css({
                        left: this.element.width() / 2 - c.width() / 2,
                        right: "auto"
                    })
            }
        },
        _effectSwitch: function (b, c) {
            a(b).hide(), a(c).css({
                left: 0
            }).show()
        },
        _effectSlide: function (b, c, d) {
            a(b).animate({
                left: this._outPosition
            }, d), a(c).css("left", -1 * this._outPosition).show().animate({
                left: 0
            }, d)
        },
        _effectSlowdown: function (b, c, d) {
            var e = {
                duration: d,
                easing: "doubleSqrt"
            };
            a.easing.doubleSqrt = function (a) {
                return Math.sqrt(Math.sqrt(a))
            }, a(b).animate({
                left: this._outPosition
            }, e), a(c).css("left", -1 * this._outPosition).show().animate({
                left: 0
            }, e)
        },
        _effectFade: function (b, c, d) {
            a(b).fadeOut(d), a(c).css({
                left: 0
            }).fadeIn(d)
        },
        _destroy: function () {},
        _setOption: function (a, b) {
            this._super("_setOption", a, b)
        }
    })
}(jQuery);