<script lang="ts" setup>
import { Input } from '@/components/ui/input'
import { Progress } from '@/components/ui/progress'
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import IconDownload from '@/components/icons/IconDownload.vue'
import InfoDiv from '@/components/InfoDiv.vue'

const progress = ref(48)
const log = ref<string>(
  '[np.float64(0.49090909090909096), np.float64(0.5333333333333334)]\n' +
    '-145.9859666170553\n' +
    '33\n' +
    '73\n' +
    '[np.float64(-1.2272727272727273), np.float64(1.5111111111111113)]\n' +
    '-107.94626055906254\n' +
    '77\n' +
    '10\n' +
    'Reached goal\n' +
    '  2%|▏         | 1/50 [00:01<00:58,  1.20s/it]Change in string: 0.1547229266\n' +
    '  4%|▍         | 2/50 [00:02<00:58,  1.23s/it]Change in string: 0.0234810466\n' +
    'Change in string: 0.0167864935\n' +
    '  8%|▊         | 4/50 [00:04<00:55,  1.22s/it]Change in string: 0.0167988143\n' +
    ' 10%|█         | 5/50 [00:06<00:55,  1.24s/it]Change in string: 0.0146997445\n' +
    ' 12%|█▏        | 6/50 [00:07<00:55,  1.27s/it]Change in string: 0.0222621052\n' +
    ' 14%|█▍        | 7/50 [00:08<00:55,  1.28s/it]Change in string: 0.0212772702\n' +
    'Change in string: 0.0275799035\n' +
    ' 18%|█▊        | 9/50 [00:11<00:51,  1.25s/it]Change in string: 0.0208653969\n' +
    ' 20%|██        | 10/50 [00:12<00:50,  1.25s/it]Change in string: 0.0331798117\n' +
    'Change in string: 0.0289484890\n' +
    ' 24%|██▍       | 12/50 [00:15<00:48,  1.28s/it]Change in string: 0.0318753745\n' +
    ' 26%|██▌       | 13/50 [00:16<00:46,  1.27s/it]Change in string: 0.0194316079\n' +
    'Change in string: 0.0268125829\n' +
    ' 30%|███       | 15/50 [00:18<00:43,  1.24s/it]Change in string: 0.0243583208\n' +
    ' 32%|███▏      | 16/50 [00:19<00:42,  1.25s/it]Change in string: 0.0223809783\n' +
    'Change in string: 0.0260810874\n' +
    ' 36%|███▌      | 18/50 [00:22<00:38,  1.22s/it]Change in string: 0.0231621049\n' +
    ' 38%|███▊      | 19/50 [00:23<00:37,  1.21s/it]Change in string: 0.0242407501\n' +
    'Change in string: 0.0230453319\n' +
    ' 42%|████▏     | 21/50 [00:25<00:33,  1.16s/it]Change in string: 0.0229965815\n' +
    ' 44%|████▍     | 22/50 [00:26<00:32,  1.15s/it]Change in string: 0.0227903015\n' +
    ' 46%|████▌     | 23/50 [00:27<00:30,  1.13s/it]Change in string: 0.0227186347\n' +
    'Change in string: 0.0222734512\n' +
    ' 50%|█████     | 25/50 [00:30<00:27,  1.11s/it]Change in string: 0.0223507579\n' +
    ' 52%|█████▏    | 26/50 [00:31<00:27,  1.13s/it]Change in string: 0.0217915914\n' +
    ' 54%|█████▍    | 27/50 [00:32<00:26,  1.15s/it]Change in string: 0.0219195806\n' +
    ' 56%|█████▌    | 28/50 [00:33<00:25,  1.16s/it]Change in string: 0.0214236857\n' +
    ' 58%|█████▊    | 29/50 [00:34<00:24,  1.16s/it]Change in string: 0.0215470950\n' +
    'Change in string: 0.0211897939\n' +
    ' 62%|██████▏   | 31/50 [00:37<00:21,  1.16s/it]Change in string: 0.0212843972\n' +
    'Change in string: 0.0210521618\n' +
    ' 66%|██████▌   | 33/50 [00:39<00:19,  1.13s/it]Change in string: 0.0211164172\n' +
    'Change in string: 0.0209742138\n' +
    ' 70%|███████   | 35/50 [00:41<00:16,  1.13s/it]Change in string: 0.0210136825\n' +
    ' 72%|███████▏  | 36/50 [00:42<00:16,  1.15s/it]Change in string: 0.0209288973\n' +
    'Change in string: 0.0209526979\n' +
    ' 76%|███████▌  | 38/50 [00:45<00:14,  1.18s/it]Change in string: 0.0209014029\n' +
    'Change in string: 0.0209159365\n' +
    ' 80%|████████  | 40/50 [00:47<00:12,  1.25s/it]Change in string: 0.0208845901\n' +
    'Change in string: 0.0208933384\n' +
    ' 84%|████████▍ | 42/50 [00:50<00:10,  1.25s/it]Change in string: 0.0208744404\n' +
    ' 86%|████████▌ | 43/50 [00:51<00:09,  1.34s/it]Change in string: 0.0208794929\n' +
    ' 88%|████████▊ | 44/50 [00:53<00:08,  1.34s/it]Change in string: 0.0208682597\n' +
    'Change in string: 0.0208711426\n' +
    ' 92%|█████████▏| 46/50 [00:55<00:05,  1.30s/it]Change in string: 0.0208645645\n' +
    'Change in string: 0.0208661367\n' +
    ' 96%|█████████▌| 48/50 [00:58<00:02,  1.39s/it]Change in string: 0.0208623256\n' +
    'Change in string: 0.0208631742\n' +
    '100%|██████████| 50/50 [01:01<00:00,  1.23s/it]\n' +
    'Change in string: 0.0208609506\n' +
    '[[ 4.71000000e-01  5.48000000e-01 -1.46650000e+02]\n' +
    ' [ 4.40291254e-01  5.39150593e-01 -1.45260115e+02]\n' +
    ' [ 3.88594043e-01  4.54361292e-01 -1.39222524e+02]\n' +
    ' [ 3.30104649e-01  3.94017541e-01 -1.33313206e+02]\n' +
    ' [ 2.63392479e-01  3.57241526e-01 -1.26042021e+02]\n' +
    ' [ 1.65061802e-01  3.33294309e-01 -1.20531661e+02]\n' +
    ' [ 1.14835757e-01  3.50349189e-01 -1.15343963e+02]\n' +
    ' [ 7.44725419e-02  3.67679105e-01 -1.10992331e+02]\n' +
    ' [ 3.51939429e-02  3.46881257e-01 -1.03257528e+02]\n' +
    ' [-4.05288065e-02  2.65356201e-01 -9.75336126e+01]\n' +
    ' [-7.95398593e-02  2.69220409e-01 -8.97063513e+01]\n' +
    ' [-1.30205244e-01  2.18307039e-01 -8.35276866e+01]\n' +
    ' [-1.80299867e-01  2.25713134e-01 -7.61841987e+01]\n' +
    ' [-2.50782616e-01  2.39348642e-01 -6.87455763e+01]\n' +
    ' [-2.55615553e-01  2.95913338e-01 -6.13047166e+01]\n' +
    ' [-3.22503486e-01  2.58093264e-01 -5.64614076e+01]\n' +
    ' [-3.52807787e-01  2.93337799e-01 -4.92493284e+01]\n' +
    ' [-3.99124456e-01  3.11142899e-01 -4.38784663e+01]\n' +
    ' [-5.07175937e-01  4.54687824e-01 -4.36850207e+01]\n' +
    ' [-5.75962027e-01  5.06035581e-01 -5.06241810e+01]\n' +
    ' [-6.93896789e-01  5.48367255e-01 -5.41109356e+01]\n' +
    ' [-7.39379847e-01  6.27970175e-01 -5.86526575e+01]\n' +
    ' [-7.85844515e-01  7.30166304e-01 -6.29288427e+01]\n' +
    ' [-8.30389038e-01  8.74446389e-01 -6.55534617e+01]\n' +
    ' [-8.60567036e-01  1.00218730e+00 -6.92595834e+01]\n' +
    ' [-9.25720388e-01  1.13174318e+00 -7.08011463e+01]\n' +
    ' [-1.03793657e+00  1.19514410e+00 -7.55819052e+01]\n' +
    ' [-1.08636214e+00  1.24491795e+00 -8.21669461e+01]\n' +
    ' [-1.08274302e+00  1.30572190e+00 -8.80458365e+01]\n' +
    ' [-1.10759911e+00  1.36239774e+00 -9.54968927e+01]\n' +
    ' [-1.19248592e+00  1.38845397e+00 -1.02173637e+02]\n' +
    ' [-1.23000000e+00  1.49400000e+00 -1.07950000e+02]]\n' +
    'The FMT time is 64.842',
)
</script>

<template>
  <article class="flex flex-col space-y-4">
    <Input
      class="border-2 border-zinc-600 rounded-lg h-full w-md mx-auto cursor-pointer"
      type="file"
    />
    <div class="font-orbitron flex space-x-8">
      <p class="w-fit text-lg text-nowrap">Figure Output</p>
      <div class="flex w-full items-center space-x-2">
        <p class="text-orange-500 text-xl select-none">{{ progress + '%' }}</p>
        <Progress v-model="progress" class="h-3" />
      </div>
    </div>
    <img class="border-4 border-zinc-500" src="/src/assets/Figure_1.png" />
    <p class="font-orbitron text-lg text-nowrap">Log Output</p>
    <InfoDiv>{{log}}</InfoDiv>
    <div class="flex">
      <Button
        class="font-orbitron m-auto mb-4 rounded-lg border-2 border-zinc-600 cursor-pointer text-orange-500 hover:text-orange-400"
        variant="outline"
      >
        <IconDownload :height="24" :width="24" />
        Figure Download
      </Button>
      <Button
        class="font-orbitron m-auto mb-4 rounded-lg border-2 border-zinc-600 cursor-pointer text-orange-500 hover:text-orange-400"
        variant="outline"
      >
        <IconDownload :height="24" :width="24" />
        Log Download
      </Button>
    </div>
  </article>
</template>

<style lang="scss" scoped></style>
