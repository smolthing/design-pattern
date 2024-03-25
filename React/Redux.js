createStore

action 
add = () => { type: ACTION}

const initialState = {};
reducer(initialState)
 case ACTION
   {...state, count: state.count + 1}

component 
onClick={add}

mapDispatchToProps

connect(mapStateToPRops, mapDispatchToProps)(Counter;)