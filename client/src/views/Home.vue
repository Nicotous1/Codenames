<style scoped>
.card {
  border: solid 1px black;
  margin: 1%;
  font-size: 2.2vw;
  cursor: pointer;
  height:98%;
  width: 18%;
  float: left;
  text-align:center;
  text-transform: capitalize;
}

button {
  margin: 10px;
}

.line {
  height:20%;
  width: 100%;
}

.frame {
  height:70vh;
  width:100%;
  max-width:2000px;
 }


.player .card.picked {
  background-color: white;
  color: black;
}

.player .blue {
  background-color: #105796;
  color: white
}

.player .red {
  background-color: #891313;
  color: white;
}

.player .black {
  background-color: #0C0C14;
  color: white;
}

.player .white {
  background-color: #ECECEC;
  color: black
}

.spy .card {
  background-color: white;
}

.spy .blue.picked {
  color: #105796;
  border: solid 3px #105796;
  background-color: white;
}

.spy .blue {
  color: white;
  border: solid 0px black;
  background-color: #105796;
}

.spy .red.picked {
  color: #891313;
  border: solid 3px #891313;
  background-color: white;
}

.spy .red {
  color: white;
  border: solid 0px black;
  background-color: #891313;
}

.spy .black.picked {
  color: black;
  border: solid 6px black;
  background-color: white;
}

.spy .black {
  color:white;
  background-color: black;
}

.spy .white.picked {
  color: gray;
  border: solid 1px gray;
  background-color: white;
}

.spy .white {
  background-color: #ECECEC;
  color:black;
  font-size: 2vw;
}

.score {
  font-weight:bold;
  font-size: 2vw;
}

.score.blue {
  color: #105796;
}

.score.red {
  color: #891313;
}

</style>

<template>
<!-- eslint-disable max-len -->
<div>

<b-container class="bv-example-row">
  <b-row class="text-center" align-v="center">
    <b-col class="score red">Rouge {{this.scores.red.k}} / {{this.scores.red.N}}</b-col>
    <b-col>
      <button type="button" class="btn btn-primary" @click="is_spy = !is_spy;">Spy Mode</button>
      <button type="button" class="btn btn-primary" @click="reset()">Reset</button>
    </b-col>
    <b-col class="score blue">Bleu {{this.scores.blue.k}} / {{this.scores.blue.N}}</b-col>
  </b-row>
</b-container>

<b-container class="frame" v-bind:class="{spy: is_spy, player: !is_spy}">
  <div class="line">
    <div v-for="card in cards" class="card" v-bind:key="card.id" v-bind:class="[card.color, {picked : card.picked}]"
    @click="setPicked(card)"
    >{{card.word}}</div>
  </div>
</b-container>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
      is_spy: false,
      cards: [],
      scores: {},
    };
  },
  methods: {
    getCards(card = 0) {
      const path = 'http://192.168.1.11:5000/cards';
      axios.get(path)
        .then((res) => {
          this.cards = res.data.cards;
          this.scores = res.data.scores;
          if (card !== 0) {
            if (card.color === 'black') {
              alert("C'est perdu !!");
            }
            if (card.color === 'red' && this.scores.red.k === this.scores.red.N) {
              alert('Les rouges ont gagné !!');
            }

            if (card.color === 'blue' && this.scores.blue.k === this.scores.blue.N) {
              alert('Les bleus ont gagné !!');
            }
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    setPicked(card) {
      if (this.is_spy) {
        return;
      }
      const path = 'http://192.168.1.11:5000/picked';
      axios.post(path, card)
        .then(() => {
          this.getCards(card);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getCards();
        });
    },
    reset() {
      const path = 'http://192.168.1.11:5000/start';
      axios.get(path)
        .then(() => {
          this.blue_win = false;
          this.red_win = false;
          this.getCards();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getCards();
        });
    },
  },
  created() {
    setInterval(this.getCards, 100);
  },
};
</script>
