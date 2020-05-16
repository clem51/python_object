{loadVideo: function (param) {
    var obj = {
        k: (hexastring = randomHexaString(0x10)),
        e: 0x3c,
        t: _0x340fef,
      },
      _0x3711c7 = this[_0x28c0("0xb7")](obj),
      xhr = new XMLHttpRequest(),
      self = this;
    xhr["addEventListener"]("abort", function () {
        self["trigger"]("callback");
    }),
      xhr["addEventListener"]("error", function () {
        self["trigger"]("callback");
      }),
      xhr["addEventListener"]("progress", function () {
        400 <= xhr["status"]
          ? self["trigger"]("callback")
          : self["function"](
              xhr["response"]["method"]()
            );
      }),
      xhr["open"]("GET", param),
      xhr[_0x28c0("0xbf")](
        "Authorization",
        _0x28c0("0xc0") + _0x3711c7
      ),
      xhr["send"]();
  }}
