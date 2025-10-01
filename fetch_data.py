import asyncio
import pandas as pd

from python_opensky import OpenSky, StatesResponse

async def main() -> None:
    async with OpenSky() as opensky:
        states: StatesResponse = await opensky.get_states()
        
        # print(states)
        # with open("states.txt", "w") as f:
        #     f.write(str(states))
        
        data_for_df = []
        if states: # Check if states is not None
            for s in states.states:
                data_for_df.append({
                    'icao24': s.icao24,
                    'callsign': s.callsign,
                    'origin_country': s.origin_country,
                    'time_position': s.time_position,
                    'last_contact': s.last_contact,
                    'longitude': s.longitude,
                    'latitude': s.latitude,
                    'geo_altitude': s.geo_altitude,
                    'on_ground': s.on_ground,
                    'velocity': s.velocity,
                    'true_track': s.true_track,
                    'vertical_rate': s.vertical_rate,
                    'sensors': s.sensors,
                    'barometric_altitude': s.barometric_altitude,
                    'transponder_code': s.transponder_code,
                    'special_purpose_indicator': s.special_purpose_indicator,
                    'position_source': s.position_source,
                    'category': s.category
                })
        df = pd.DataFrame(data_for_df)
        df.fillna(value=pd.NA, inplace=True) # Replace None with pandas' NA
 
        df.to_csv("flight_data.csv")
        
        
if __name__ == "__main__":
    asyncio.run(main())