$(document).ready(function() {
  var apiKey = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjcyMzExMDc4MmVmMGM3YTdmNjliN2EyZDY5MDQxZDBkM2IxNzQ3ZjkwMTA1NWNmZTVlNDY2N2NhOGY2OTFkOGVhMTlkNjk0ZWQ1YmNmYjc1In0.eyJhdWQiOiIyMDM4NCIsImp0aSI6IjcyMzExMDc4MmVmMGM3YTdmNjliN2EyZDY5MDQxZDBkM2IxNzQ3ZjkwMTA1NWNmZTVlNDY2N2NhOGY2OTFkOGVhMTlkNjk0ZWQ1YmNmYjc1IiwiaWF0IjoxNjcxMjcxMzY1LCJuYmYiOjE2NzEyNzEzNjUsImV4cCI6MTY3Mzc3Njk2NSwic3ViIjoiIiwic2NvcGVzIjpbImJhc2ljIl19.PI3vHjsfRB98fNvgm93prSCpA3S_0-mcLQlmwTmDfcQ8cSMOIUdoJcJ6P9Mi_XQ4m_uU0UE-DLy_54Dz2BAjvhq9Ah1KVRC2Svgs7Kck8MAn_xILI0K3PxSr_GFuUXOAK0FR29KhhvwBpqQdnC76Bl5dfpInooCSeSvFvUKuUC3d8QF9pDc6FHuqRsuM9x1uhRbv1TpRZMo2uXiXClwjHH_uvOwurrC9EfDYcXFw72sMeIi90COuspoUUJCnZF1MGH0JR9DUK9oyEDVbf0uA9PnIULr6J98lq82aAQrFlDeD389GHtQ131uNhZV1WUBclseQQYFSiXjZ5AZ_qbukyg"
  var app = new Mapp({
    element: "#app",
    presets: {

      latlng: {
        lat: 30.28433719869416,
        lng: 57.04943977296354

      },
      zoom: 6
    },
    locale: "fa",
    apiKey
  });

  app.addLayers();

  var start = {};
  var end = {};
  var index = 1;
  var curse = 0;
  var history = [];
  var trollTimeout;
  var memeTimeout;

  kickOff();

 

  $(".app-reset button").on("click", function() {
    $(".app-results-ul").html("");

    if (start.marker) app.map.removeLayer(start.marker);
    if (end.marker) app.map.removeLayer(end.marker);


    $(".app-end").remove();

    index = 1;
    curse = 0;
    history = [];

    app.removeRoute();

    kickOff();
  });

  app.map.on("click", function() {
    leg("روی نقشه کلیک شد.");
  });

  function kickOff() {
    leg(
      "در این دمو یک نقطه ابتدایی و یک نقطه انتهایی از کاربر گرفته و مسیر بین این دو نقطه کشیده میشه. با توجه به اتنخاب کاربر این مسیر میتونه یکی از چند روع «رانندگی با خودرو»، «پیاده»، یا «دوچرخه سواری» باشه."
    );
      

    start = {
      latlng: undefined,
      marker: undefined,
      icon: {
        iconUrl: "./app/assets/images/marker-default-blue.svg",
        iconSize: [40, 40],
        iconAnchor: [20, 40],
        popupAnchor: [0, -40]
      }
    };

    end = {
      latlng: undefined,
      marker: undefined,
      icon: {
        iconUrl: "./app/assets/images/marker-default-red.svg",
        iconSize: [40, 40],
        iconAnchor: [20, 40],
        popupAnchor: [0, -40]
      }
    };

    app.map.fitBounds([[35.532, 51.051], [35.835, 51.632]]);

    leg("در حال تلاش برای پیدا کردن موقعیت فعلی کاربر...");

    app.getUserLocation({
      before: function() {
        freeze();
      },
      after: function() {
        unfreeze();
      },
      success: function() {
        start.latlng = app.map.getCenter();
        start.marker = app.addMarker({
          name: "start",
          latlng: start.latlng,
          icon: start.icon,
          popup: false,
          pan: false,
          draggable: true,
          history: false
        });
        leg("موقعیت کاربر پیدا شد.");

        app.map.panTo({
          lat: app.states.user.latlng.lat,
          lng: app.states.user.latlng.lng
        });

        leg("نقشه به موقعیت کاربر حرکت داده شد.");

        $("#mapp-app").append('<div class="app-end"></div>');
        leg(
          "می‎توانید نقشه را حرکت داده و برای ثبت نقطه شروع روی مارکر کلیک کنید."
        );
        leg("منتظر تصمیم شما...");

          $(".app-end").on("click", function() {

            end.latlng = app.map.getCenter();

            end.marker = app.addMarker({
              name: "end",
              latlng: end.latlng,
              icon: end.icon,
              popup: false,
              pan: false,
              draggable: true,
              history: false
            });

            leg("نقطه پایان ثبت شد.");

            $(".app-end").remove();

            end.marker.on("dragend", function() {
              leg("نقطه پایان تغییر کرد.");

              end.latlng = end.marker.getLatLng();

              doRoute();
            });

            doRoute();
          });
          
      },
      error: function() {
        leg("آخ، نشد که جاش پیدا بشه. حالا میگی چیکار کنیم؟");
        troll("7");
      },
      pan: false,
      marker: false
    });
  }

  function leg(text) {
    var printed = text;

    if (text === history[history.length - 1]) {
      printed = "برای بار دوم، " + text;

      if (text === history[history.length - 2]) {
        printed =
          curse < 2
            ? "گیر دادی ها!!! میگم " + text
            : "گرفتاری شدیم این وقت شب...";

        if (curse === 2) meme("parviz");

        if (curse < 2 && text === history[history.length - 3]) {
          printed = "تو بی‎خیال نمی‎شی، نه؟";
          troll("4");

          if (text === history[history.length - 4]) {
            printed = "هوممم";
            troll("2");

            if (text === history[history.length - 5]) {
              printed = "یکی این اسباب بازی رو از دست این بچه بگیره!";
              troll("7");

              if (text === history[history.length - 6]) {
                curse = 1;
                printed = "بسه دیگه...";
                troll("1");

                if (text === history[history.length - 7]) {
                  printed = "یعنی چی آخه؟!";
                  troll("6");

                  if (text === history[history.length - 8]) {
                    printed = "%^&@#!";
                    troll("3");

                    if (text === history[history.length - 9]) {
                      printed = "خودتی";
                      troll("5");

                      if (text === history[history.length - 10]) {
                        troll();

                        return;
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

    if (
      curse === 1 &&
      history[history.length - 1] !== undefined &&
      text !== history[history.length - 1]
    ) {
      history = [];
      curse = 2;
      index = 1;
      printed = "برگردیم سر نقشه. " + text;

      $(".app-results-ul").html("");
    }

    history.push(text);

    var html =
      '<li class="app-results-li highlighted" id="li-' +
      index +
      '">' +
      '<div class="app-result-content">' +
      index +
      " - " +
      printed +
      "</div>" +
      "</li>";

    $(".app-results-ul").prepend(html);

    var i = index;

    setTimeout(function() {
      $("#li-" + i).removeClass("highlighted");
    }, 2000);

    index += 1;
  }

  function doRoute() {
    if (start.latlng && end.latlng) {
      leg("در حال پیدا کردن مسیر...");

      var result = app.drawRoute({
        before: function() {
          freeze();
        },
        after: function() {
          unfreeze();

          leg(result.length + " مسیر پیدا شد.");

          $.each(result, function(index, item) {
         
            console.log( 
                "مسیر " +
                (index + 1) +
                " از [" +
                start.latlng.lat.toFixed(5) +
                ", " +
                start.latlng.lng.toFixed(5) +
                "] به [" +
                end.latlng.lat.toFixed(5) +
                ", " +
                end.latlng.lng.toFixed(5) +
                "] به طول " +
                item.distance +
                " متر و مدت تقریبی " +
                Math.ceil(item.duration / 60) +
                " دقیقه.");
          });

          leg(
            "می‎توانید نقاط ابتدایی یا انتهایی مسیر را روی نقشه حرکت دهید، یا برای شروع مجدد روی دکمه «از نو» کلیک کنید."
          );
        },
     
        start: {
          lat: 30.28433719869416,
          lng: 57.04943977296354
  
        },
        end: end.latlng,
        mode: $('[name="type"]')
          .filter(":checked")
          .val(),
        draggable: true,
        fit: true,
        colors: ["#F44336", "#607D8B", "#FF9800"],
        select: {
          enabled: false
        }
      });
      console.log('-----------------------');
      console.log(start.latlng);
    }
  }

  function troll(image) {
    if (!image) var image = Math.ceil(Math.random() * 7);
    if (trollTimeout) clearTimeout(trollTimeout);

    $(".app-troll").addClass("app-visible");
    $(".app-troll").css({
      backgroundImage: "var(--troll-" + image + ")",
      transform:
        "translate(-50%, -50%) rotate(" +
        Math.ceil(Math.random() * 60 - 30) +
        "deg)"
    });

    trollTimeout = setTimeout(function() {
      $(".app-troll").removeClass("app-visible");
    }, 1000);
  }

  function meme(image) {
    if (memeTimeout) clearTimeout(memeTimeout);

    $(".app-meme").addClass("app-visible");
    $(".app-meme").css({
      backgroundImage: "var(--meme-" + image + ")"
    });

    memeTimeout = setTimeout(function() {
      $(".app-meme").removeClass("app-visible");
    }, 1000);
  }

  function unfreeze() {
    $(".app-overlay").removeClass("app-visible");
    $("textarea").prop("disabled", false);
    $("button").prop("disabled", false);
    $("input").prop("disabled", false);
  }

  function freeze() {
    $(".app-overlay").addClass("app-visible");
    $("textarea").prop("disabled", true);
    $("button").prop("disabled", true);
    $("input").prop("disabled", true);
  }
console.log($("#type-12")[0]);
});
