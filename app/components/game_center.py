import streamlit as st
import random
import time

def game_center_page():
    tab1, tab2 = st.tabs(["Memory Matcher", "Rock Paper Scissors"])

    with tab1:
        _memory_matcher_game()
    with tab2:
        _rock_paper_scissors_game()

def _memory_matcher_game():
    st.title("🧠 Memory Matcher")
    
    if 'game_state' not in st.session_state:
        _initialize_memory_game()
    
    game = st.session_state.game_state
    _display_memory_game_grid(game)
    _check_win_condition(game)

def _initialize_memory_game():
    emojis = ['🍎', '🍌', '🍇', '🍊', '🍉', '🍓', '🚗', '🚀', '🎈', '🏀', '🐶', '🐱']
    board = emojis * 2
    random.shuffle(board)
    
    st.session_state.game_state = {
        'board': board,
        'flipped': [],
        'matched': [],
        'attempts': 0,
        'game_over': False
    }

def _display_memory_game_grid(game):
    cols = st.columns(4)
    for i in range(12):
        with cols[i % 4]:
            if i not in game['matched']:
                if i in game['flipped']:
                    st.button(game['board'][i], disabled=True, key=f"flipped_{i}")
                else:
                    if st.button(f"Card {i+1}", key=f"card_{i}"):
                        _handle_card_click(game, i)
            else:
                st.button(game['board'][i], disabled=True, key=f"matched_{i}")

def _handle_card_click(game, index):
    game['flipped'].append(index)
    if len(game['flipped']) == 2:
        game['attempts'] += 1
        _check_match(game)

def _check_match(game):
    first, second = game['flipped']
    if game['board'][first] == game['board'][second]:
        game['matched'].extend(game['flipped'])
    else:
        time.sleep(1)
    game['flipped'] = []

def _check_win_condition(game):
    st.write(f"Attempts: {game['attempts']}")
    if len(game['matched']) == 12:
        st.balloons()
        st.success("Congratulations! You found all pairs! 🎉")
        game['game_over'] = True
        if st.button("New Game", key="new_game"):
            del st.session_state.game_state

def _rock_paper_scissors_game():
    st.title("✊ Rock Paper Scissors Showdown!")
    _init_rps_styles()
    
    choices = ['Rock ✊', 'Paper ✋', 'Scissors ✌️']
    player_choice = st.radio("Make your choice", choices)

    if st.button("Play"):
        _play_rps_round(player_choice, choices)

def _init_rps_styles():
    st.markdown("""
        <style>
        .hand-container {
            display: flex;
            justify-content: space-between;
            font-size: 100px;
            margin: 20px 0;
            transition: transform 0.3s ease;
        }
        .hand-move {
            animation: shake 0.5s;
        }
        @keyframes shake {
            0% { transform: rotate(0deg); }
            25% { transform: rotate(15deg); }
            50% { transform: rotate(-15deg); }
            75% { transform: rotate(15deg); }
            100% { transform: rotate(0deg); }
        }
        </style>
    """, unsafe_allow_html=True)

def _play_rps_round(player_choice, choices):
    computer_choice = random.choice(choices)
    
    with st.spinner('Battling it out...'):
        time.sleep(1)

    col1, col2 = st.columns(2)
    with col1:
        st.write("### Your Choice")
        st.markdown(f"## {player_choice}")
    with col2:
        st.write("### Computer's Choice")
        st.markdown(f"## {computer_choice}")

    _determine_winner(player_choice, computer_choice)

def _determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        st.balloons()
        st.info("### It's a tie! 🤝")
    elif (
        (player_choice == 'Rock ✊' and computer_choice == 'Scissors ✌️') or
        (player_choice == 'Paper ✋' and computer_choice == 'Rock ✊') or
        (player_choice == 'Scissors ✌️' and computer_choice == 'Paper ✋')
    ):
        st.snow()
        st.success("### You win! 🎉🏆")
    else:
        st.error("### Computer wins! That's always OK, TRY AGAIN! 😢🤖") 