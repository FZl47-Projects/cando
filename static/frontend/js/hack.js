Mapp.prototype.drawRoute = function(opt){
	this.icons.circle = {
		white: {
			iconUrl: mappWd + 'assets/images/marker-circle-white.svg',
			iconSize: [8, 8],
			iconAnchor: [4, 4],
			popupAnchor: [0, -4]
		},
	};

	var options = $.extend(true, {
		before: function(){},
		after: function(){},
		start: {},
		end: {},
		mode: 'car',
		draggable: true,
		styles: {
			core: {
				weight: 3,
				opacity: 1,
			},
			shadow: {
				weight: 11,
				opacity: .3,
			},
		},
		colors: ['#F44336', '#FF9800', '#607D8B'],
		select: {
			enabled: true,
			color: '#2196F3',
		},
		fit: true,
	}, opt);

	if($.type(options.start) === 'undefined' || $.type(options.end) === 'undefined') return;

	if ($.type(options.start) === 'object') options.start = [options.start.lat, options.start.lng];
	if ($.type(options.end) === 'object') options.end = [options.end.lat, options.end.lng];

	options.mode = (options.mode === 'foot') ? 'foot' : (options.mode === 'bicycle') ? 'bicycle' : 'route';

	this.groups.route = this.groups.route || {
		whole: L.featureGroup(),
		nodes: [],
		lines: [],
	}

	var _this = this;
	var output = [];
	var bounds;

	options.before();

	this.ajax({
		mode: this.env.mode,
		task: 'route',
		url: this.env.url.route + '/' + options.mode + '/v1/driving/' + [options.start[1], options.start[0]].join(',') + ';' + [options.end[1], options.end[0]].join(','),
		type: 'GET',
		data: {
			alternatives: true,
			steps: true,
			overview: 'false',
			hints: ';'
		},
		dataType: 'json',
		success: function(data) {
			if (data.code !== 'Ok') return;

			_this.removeRoute();

			$.each(data.routes, function(index, value) {
				_this.groups.route.nodes[index] = L.featureGroup();
				_this.groups.route.lines[index] = L.featureGroup();

				options.styles.core.color = options.colors[index] || options.colors[options.colors.length - 1];
				options.styles.shadow.color = options.colors[index] || options.colors[options.colors.length - 1]

				if (index !== 0) {
					options.styles.core.dashArray = "10 10";
					options.styles.shadow.dashArray = "10 10";
				} else {
					options.styles.core.dashArray = undefined;
					options.styles.shadow.dashArray = undefined;
				}

				if (data.waypoints !== undefined) {
					L.polyline([[options.start[0], options.start[1]], [data.waypoints[0].location[1], data.waypoints[0].location[0]]], options.styles.shadow).addTo(_this.groups.route.whole).addTo(_this.groups.route.lines[index]);
					L.polyline([[options.start[0], options.start[1]], [data.waypoints[0].location[1], data.waypoints[0].location[0]]], options.styles.core).addTo(_this.groups.route.whole).addTo(_this.groups.route.lines[index]);

					L.polyline([[options.end[0], options.end[1]], [data.waypoints[1].location[1], data.waypoints[1].location[0]]], options.styles.shadow).addTo(_this.groups.route.whole).addTo(_this.groups.route.lines[index]);
					L.polyline([[options.end[0], options.end[1]], [data.waypoints[1].location[1], data.waypoints[1].location[0]]], options.styles.core).addTo(_this.groups.route.whole).addTo(_this.groups.route.lines[index]);
				}

				$.each(value.legs[0].steps, function(id, val) {
					var popupText = '<div class="feature-popup">' + (val.name || '') + '</div>';

					L.polyline(polyline.decode(val.geometry), options.styles.shadow).addTo(_this.groups.route.whole).addTo(_this.groups.route.lines[index]);
					L.polyline(polyline.decode(val.geometry), options.styles.core).addTo(_this.groups.route.whole).addTo(_this.groups.route.lines[index]);

					L.marker([val.maneuver.location[1], val.maneuver.location[0]], {
						icon: L.icon(_this.icons.circle.white),
					}).addTo(_this.groups.route.whole).addTo(_this.groups.route.nodes[index]).bindPopup(popupText, _this.popupOptions);

					bounds = _this.groups.route.whole.getBounds();
				});

				_this.groups.route.nodes[index].addTo(_this.map);
				_this.groups.route.lines[index].addTo(_this.map);

				output.push({
					featureGroups: {
						nodes: _this.groups.route.nodes[index],
						lines: _this.groups.route.lines[index],
					},
					distance: value.distance,
					duration: value.duration,
				});

				if(options.select.enabled) _this.groups.route.lines[index].on('click', function(event){
					event.originalEvent.stopPropagation();
					event.originalEvent.preventDefault();

					_this.colorRoute();

					_this.groups.route.lines[index].setStyle({
						color: options.select.color,
					});
				});
			});

			if(options.fit === true) _this.map.fitBounds(bounds);

			options.after();
		}
	});

	return output;
}

Mapp.prototype.removeRoute = function(opt){
	var options = $.extend(true, {
		before: function(){},
		after: function(){},
	}, opt);

	var _this = this;

	if(!_this.groups.route) return;

	$.each(_this.groups.route.lines, function(index, item){
		if(_this.groups.route.lines[index]) _this.groups.route.lines[index].clearLayers();
	});

	$.each(_this.groups.route.nodes, function(index, item){
		if(_this.groups.route.nodes[index]) _this.groups.route.nodes[index].clearLayers();
	});

	if(_this.groups.route) _this.groups.route.whole.clearLayers();

	this.groups.route = {
		whole: L.featureGroup(),
		nodes: [],
		lines: [],
	}
}

Mapp.prototype.colorRoute = function(opt){
	var options = $.extend(true, {
		colors: ['#F44336', '#FF9800', '#607D8B'],
	}, opt);

	var _this = this;

	$.each(_this.groups.route.lines, function(id, val) {
		val.setStyle({
			color: options.colors[id] || options.colors[options.colors.length - 1],
		});
	});
}




Mapp.prototype.icons.geolocation = {
	iconUrl: mappWd + 'assets/images/marker-default-red.svg',
	iconSize: [40, 40],
	iconAnchor: [20, 40],
	popupAnchor: [0, -40],
};

Mapp.prototype.addGeolocation = function(opt){
	var options = $.extend(true, {
		history: false,
		onLoad: false,
		onLoadCallback: function(){},
	}, opt);

	var _this;

	var htmlDesktop = '<div class="icon-background is-lighter is-rounded is-boxed margined-large"><a data-i18n="[title]mapp-tooltip-geolocation" href="#" class="icon is-large icon-geolocation desktop tooltip-right"></a></div>';
	var htmlTabletMobile = '<div class="icon-background is-lighter is-rounded is-boxed margined-small"><a data-i18n="[title]mapp-tooltip-geolocation" href="#" class="icon is-large icon-geolocation tablet mobile tooltip-left"></a></div>';

	this.dom.footer.triggers.right.append(htmlTabletMobile);
	this.dom.footer.triggers.left.append(htmlDesktop);

	var triggerGeolocation = $(this.settings.element).find('.icon-geolocation');

	_this = this;

	triggerGeolocation.on('click', function(event) {
		event.preventDefault();
		event.stopPropagation();

		_this.getUserLocation();
	});

	if(options.onLoad) this.getUserLocation({
		success: options.onLoadCallback,
	});
}

Mapp.prototype.getUserLocation = function(opt){
	var options = $.extend(true, {
		before: function(){},
		after: function(){},
		success: function(){},
		error: function(){},
		pan: true,
		marker: true,
	}, opt);

	var _this;

	options.before();

	this.map.locate({
		// watch: true,
	});

	_this = this;

	this.map.off('locationfound').on('locationfound', function(event){
		_this.updateStateUser(event.latlng);

		_this.geolocationSuccess({
			event: event,
			pan: options.pan,
			marker: options.marker,
		});

		options.success();

		options.after();
	});

	this.map.off('locationerror').on('locationerror', function(event){
		_this.geolocationError({
			event: event,
		});

		options.error();

		options.after();
	});
}

Mapp.prototype.geolocationSuccess = function(opt){
	var options = $.extend(true, {
		event: {},
		pan: true,
		marker: true,
	}, opt);

	var radius = options.event.accuracy / 2;

	if(options.pan){
		this.map.setView(options.event.latlng, 16);

		this.updateStateCurrent();
	}

	if(options.marker){
		var _this;

		_this = this;

		this.addMarker({
			name: 'geolocation',
			latlng: this.states.user.latlng,
			icon: this.icons.geolocation,
			popup: {
				title: {
					html: '<span data-i18n="mapp-my-location"></span>',
					i18n: '',
				},
				description: {
					html: _this.generateLatlngHtml({
						lat: parseFloat(_this.states.user.latlng.lat),
						lng: parseFloat(_this.states.user.latlng.lng),
						type: 'block',
					}),
					i18n: '',
				},
				open: true,
			},
			pan: false,
			history: false,
		});
	}
}

Mapp.prototype.geolocationError = function(opt){
	var options = $.extend(true, {
		event: {},
	}, opt);
}
