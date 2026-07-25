import streamlit as st
import numpy as np

# -----------------------------
# Initialize Session State
# -----------------------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "winner" not in st.session_state:
    st.session_state.winner = None


# -----------------------------
# Winner Function
# -----------------------------
def check_winner(board):

    if 3 in np.sum(board, axis=1) or 3 in np.sum(board, axis=0):
        return "X"

    if -3 in np.sum(board, axis=1) or -3 in np.sum(board, axis=0):
        return "O"

    if np.trace(board) == 3 or np.trace(np.fliplr(board)) == 3:
        return "X"

    if np.trace(board) == -3 or np.trace(np.fliplr(board)) == -3:
        return "O"

    if not 0 in board:
        return "DRAW"

    return None


# -----------------------------
# Convert Number to Symbol
# -----------------------------
def symbol(value):
    if value == 1:
        return "❌"
    elif value == -1:
        return "⭕"
    return " "


# -----------------------------
# Button Click
# -----------------------------
def make_move(row, col):

    if st.session_state.game_over:
        return

    if st.session_state.board[row][col] != 0:
        return

    st.session_state.board[row][col] = st.session_state.current

    result = check_winner(st.session_state.board)

    if result:
        st.session_state.game_over = True
        st.session_state.winner = result
    else:
        st.session_state.current *= -1


# -----------------------------
# Reset Game
# -----------------------------
def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False
    st.session_state.winner = None


# -----------------------------
# UI
# -----------------------------
st.title("🎮 Tic Tac Toe")

if not st.session_state.game_over:
    player = "❌ X" if st.session_state.current == 1 else "⭕ O"
    st.subheader(f"Current Player : {player}")
else:
    if st.session_state.winner == "DRAW":
        st.success("🤝 It's a Draw!")
    else:
        st.success(f"🎉 {st.session_state.winner} Wins!")


# -----------------------------
# Game Board
# -----------------------------
for i in range(3):

    cols = st.columns(3)

    for j in range(3):

        cols[j].button(
            symbol(st.session_state.board[i][j]),
            key=f"{i}-{j}",
            on_click=make_move,
            args=(i, j),
            use_container_width=True,
            disabled=st.session_state.game_over,
        )

st.write("")

if st.button("🔄 New Game", use_container_width=True):
    reset_game()
    st.rerun()