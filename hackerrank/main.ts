// const ranked = [100,90,90,80];
// const player = [70,80,105];
const ranked = [100, 100, 50, 40, 40, 20, 10];
const places = [1, 1, 2, 3, 3, 4, 5]; // TODO: calculate this
const player = [5, 25, 50, 120];

interface Result {
    boardIdx: number;
    place: number;
}

interface Leaderboard {
    scores: number[];
    places: number[];
    length: number;
}

const getResult = (leaderboard: Leaderboard, score: number): Result => {
    let minIdx = 0;
    let maxIdx = leaderboard.length - 1;

    // Binary search, go to the right on ties
    while (maxIdx >= minIdx) {
        const testIdx = Math.floor((minIdx + maxIdx) / 2);
        const testScore = leaderboard.scores[testIdx];
        console.log(minIdx, testIdx, maxIdx, score, testScore);
        if (score <= testScore) {
            minIdx = testIdx + 1;
        } else {
            maxIdx = testIdx - 1;
        }
    }

    let place = 1;
    if (minIdx > 0) {
        place = leaderboard.places[minIdx - 1];
        if (score !== leaderboard.scores[minIdx - 1]) {
            place++;
        }
    }

    return { boardIdx: minIdx, place };
};


const buildLeaderboard = (scores: number[]): Leaderboard => {
    const places = [];

    if (scores.length > 0) {
        let place = 1;
        let [last, ...rest] = scores;
        places.push(place);
    
        for (const score of scores) {
            if (last !== score) {
                place++;
            }
            places.push(place);
            last = score;
        }
    }

    return {
        scores,
        places,
        length: scores.length,
    };
};

const leaderboard = buildLeaderboard(ranked);
console.log('110 is', getResult(leaderboard, 110));
console.log('5 is', getResult(leaderboard, 5));
console.log('100 is', getResult(leaderboard, 100));
console.log('10 is', getResult(leaderboard, 10));
console.log('40 is', getResult(leaderboard, 40));
console.log('30 is', getResult(leaderboard, 30));

