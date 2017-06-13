Title: Model comparison
Date: 2017-06-12 10:20
url: plots.html
save_as: plots.html

<script>
var url = new URL(window.location);
var usecase = url.searchParams.get("usecase");
var stage = url.searchParams.get("stage");
console.log("Plotting usecase, stage:", usecase, stage);
</script>

### Time series output

<select onChange="document.getElementById('timeseries').src='images/usecase'+usecase+'_stage'+stage+'_'+this.value+'.jpg'">
<option value="ldw"  >  long wave downward radiation at surface  </option>
<option value="lup"  >  long wave upward radiation at surface    </option>
<option value="qdw"  >  short wave downward radiation at surface </option>
<option value="qup"  >  short wave upward radiation at surface   </option>
<option value="tsk"  >  temperature skin layer                   </option>
<option value="g"    >  soil heat flux                           </option>
<option value="shf"  >  sensible heat flux                       </option>
<option value="lhf"  >  latent heat flux                         </option>
<option value="qf"   >  anthropogenic heat flux                  </option>
<option value="ustar">  friction velocity                        </option>
<option value="hpbl" >  boundary layer height                    </option>
<option value="t2m"  >  2m temperature                           </option>
<option value="q2m"  >  2m specific humidity                     </option>
<option value="u10m" >  10m u-component wind                     </option>
<option value="v10m" >  10m v-component wind                     </option>
<option value="cc"   >  cloud cover fraction                     </option>
</select>

<img id="timeseries" src="" alt="plot of time series output" style="width=100%">

### Mean state

<select onChange="document.getElementById('meanstate').src='images/usecase'+usecase+'_stage'+stage+'_'+this.value+'.jpg'">
<option value="zf" > height of full level       </option>
<option value="pf" > pressure at full level     </option>
<option value="t"  > temperature                </option>
<option value="th" > potential temperature      </option>
<option value="q"  > specific humidity          </option>
<option value="u"  > zonal component wind       </option>
<option value="v"  > meridional component wind  </option>
</select>

<img id="meanstate" src="" alt="plot of mean state" style="width=100%">

### Prescribed forcings

<select onChange="document.getElementById('forcings').src='images/usecase'+usecase+'_stage'+stage+'_'+this.value+'.jpg'">
<option value="ugeo"    > u-component geostrophic wind    </option>
<option value="vgeo"    > v-component geostrophic wind    </option>
<option value="dudt_ls" > u-component momentum advection  </option>
<option value="dvdt_ls" > v-component momentum advection  </option>
<option value="dtdt_ls" > temperature advection           </option>
<option value="dqdt_ls" > moisture advection              </option>
<option value="ome"     > vertical movement               </option>
</select>

<img id="forcings" src="" alt="plot of prescribed forcings" style="width=100%">

### Fluxes

<select onChange="document.getElementById('fluxes').src='images/usecase'+usecase+'_stage'+stage+'_'+this.value+'.jpg'">
<option value="zh"   > height of half level                </option>
<option value="ph"   > pressure at half level              </option>
<option value="wt"   > vertical temperature flux           </option>
<option value="wq"   > vertical moisture flux              </option>
<option value="uw"   > vertical flux u-component momentum  </option>
<option value="vw"   > vertical flux v-component momentum  </option>
<option value="Km"   > eddy diffusivity momentum           </option>
<option value="Kh"   > eddy diffusivity heat               </option>
<option value="TKE"  > turbulent kinetic energy            </option>
<option value="shear"> shear production                    </option>
<option value="buoy" > buoyancy production                 </option>
<option value="trans"> total transport                     </option>
<option value="dissi"> dissipation                         </option>
</select>

<img id="fluxes" src="" alt="plot of fluxes" style="width=100%">

### Soil variables

<select onChange="document.getElementById('soil').src='images/usecase'+usecase+'_stage'+stage+'_'+this.value+'.jpg'">
<option value="zs"  > height of soil level   </option>
<option value="ts"  > soil temperature       </option>
<option value="ths" > soil water content     </option>
</select>

<img id="soil" src="" alt="plot of soil variables" style="width=100%">

