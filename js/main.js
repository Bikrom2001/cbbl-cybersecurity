/* CBBL interactions — Bootstrap 5 Compatible */
(function () {
  "use strict";

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* Search Modal Auto-focus */
  var searchModal = document.getElementById("searchModal");
  if (searchModal) {
    searchModal.addEventListener("shown.bs.modal", function () {
      var input = document.getElementById("searchInput");
      if (input) input.focus();
    });
  }

  /* Cookie banner */
  var cookie = document.getElementById("cookieBanner");
  var KEY = "cbbl_cookie_choice";
  try {
    if (cookie && !localStorage.getItem(KEY)) {
      cookie.classList.add("is-visible");
    }
  } catch (err) {
    if (cookie) cookie.classList.add("is-visible");
  }

  $$("[data-cookie]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      try {
        localStorage.setItem(KEY, btn.getAttribute("data-cookie"));
      } catch (err) {}
      if (cookie) cookie.classList.remove("is-visible");
    });
  });

  /* Course / catalogue filter */
  $$("[data-filter-group]").forEach(function (group) {
    var targetSel = group.getAttribute("data-target");
    group.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-filter]");
      if (!btn) return;
      var value = btn.getAttribute("data-filter");
      $$("[data-filter]", group).forEach(function (b) {
        b.setAttribute("aria-pressed", b === btn ? "true" : "false");
      });
      $$(targetSel + " [data-category]").forEach(function (card) {
        var match = (value === "all" || card.getAttribute("data-category") === value);
        card.classList.toggle("d-none", !match);
      });
      var count = $$(targetSel + " [data-category]").filter(function (c) {
        return !c.classList.contains("d-none");
      }).length;
      var out = $("[data-result-count]");
      if (out) out.textContent = count + (count === 1 ? " course" : " courses");
    });
  });

  /* Forms: Bootstrap validation + demo success */
  $$("form[data-demo-form]").forEach(function (form) {
    var success = form.querySelector(".form-success");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var bad = null;
      var inputs = form.querySelectorAll("[required]");
      inputs.forEach(function (input) {
        var ok = input.type === "checkbox" ? input.checked : input.value.trim() !== "";
        if (input.type === "email" && ok) {
          ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim());
        }
        input.classList.toggle("is-invalid", !ok);
        if (!ok && !bad) bad = input;
      });

      if (bad) {
        bad.focus();
        return;
      }

      var ref = "CBBL-" + new Date().getFullYear() + "-" + String(Math.floor(Math.random() * 9000) + 1000);
      if (success) {
        success.classList.add("is-visible");
        var refEl = success.querySelector("[data-ref]");
        if (refEl) refEl.textContent = ref;
        success.setAttribute("tabindex", "-1");
        success.focus();
        success.scrollIntoView({ block: "center", behavior: "smooth" });
      }
      form.reset();
      inputs.forEach(function (input) {
        input.classList.remove("is-invalid");
      });
    });

    form.querySelectorAll("input, select, textarea").forEach(function (input) {
      input.addEventListener("input", function () {
        input.classList.remove("is-invalid");
      });
    });
  });

  /* Table of contents highlight */
  var subnavLinks = $$(".subnav a[href^='#']");
  if (subnavLinks.length && "IntersectionObserver" in window) {
    var map = {};
    subnavLinks.forEach(function (a) {
      map[a.getAttribute("href").slice(1)] = a;
    });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          subnavLinks.forEach(function (a) { a.removeAttribute("aria-current"); });
          var link = map[en.target.id];
          if (link) link.setAttribute("aria-current", "true");
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px" });

    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) obs.observe(el);
    });
  }

  /* Dynamic Year */
  $$("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
