/*!
  @brief Compute the intensity of light.

  @param[in] doy Day of year including partial days.
  @param[in] geom 3D geometry of plant
  @param[out] intensity Intensity of light in ergs s^-1.

  @returns Success (1) or failure (0).
 */
int light(double doy, rapidjson::ObjWavefront geom,
	  double* intensity) {
  // Define parameters that are static across a run
  double amplitude = 6.0e-4;
  double doy_offset = 0.0;

  // Calculate total intensity on each leaf
  intensity[0] = 0.0;
  std::vector<double> areas = geom.areas();
  for (std::vector<double>::iterator it = areas.begin();
       it != areas.end(); it++) {
    intensity[0] += *it * amplitude
      * (0.5 + 0.5 * sin(2.0 * M_PI * (floor(doy) - doy_offset) / 365))
      * (0.5 + 0.5 * cos(2.0 * M_PI * (std::fmod(doy, 1.0) - 0.5)));
  }

  // Return success
  return 1;
}
