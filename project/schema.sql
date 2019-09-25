CREATE TABLE vehicle(
	case_VID VARCHAR(10) UNIQUE PRIMARY KEY,
	body_type VARCHAR(128),
	reg_class VARCHAR(128),
	axles VARCHAR(128),
	fuel_type VARCHAR(128),
	vehicle_year INTEGER,
	reg_state VARCHAR(128),
	engine_cylinder VARCHAR(128),
	vehicle_make VARCHAR(128),
	partial_vin VARCHAR(128)
);

CREATE TABLE event(
	case_VID VARCHAR(10) REFERENCES vehicle(case_VID),
	seating_pos VARCHAR(128),
	ejection VARCHAR(128),
	safety_equip VARCHAR(128),
	action_prior VARCHAR(256),
	direction VARCHAR(128),
	number_occup INTEGER,
	event_type VARCHAR(128),
	year INTEGER
);

CREATE TABLE victim(
	case_IID VARCHAR(10) UNIQUE,
	case_VID VARCHAR(10) REFERENCES vehicle(case_VID),
	role_type VARCHAR(256),
	lic_state VARCHAR(128),
	sex VARCHAR(128),
	age INTEGER,
	PRIMARY KEY(case_IID, case_VID)
);

CREATE TABLE cause(
	case_VID VARCHAR(10) REFERENCES vehicle(case_VID),
	factor1 VARCHAR(256),
	factor1_desc VARCHAR(256),
	factor2 VARCHAR(256),
	factor2_desc VARCHAR(256)
);

CREATE TABLE injury(
	case_IID VARCHAR(10) REFERENCES victim(case_IID),
	victim_status VARCHAR(128),
	injury_desc VARCHAR(256),
	injury_location VARCHAR(128),
	injury_sev VARCHAR(128)
	
);
