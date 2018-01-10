syntax enable

:set tabstop=2
:set shiftwidth=2
:set expandtab

set number

set guioptions-=m  "menu bar
set guioptions-=T  "toolbar
set guioptions-=r  "scrollbar

set rtp+=$HOME/.vim/bundle/Vundle.vim/
call vundle#begin('$HOME/.vim/bundle/')
  Plugin 'VundleVim/Vundle.vim'
  Plugin 'scrooloose/nerdtree'
  " Plugin 'valloric/youcompleteme'
  Plugin 'mattn/emmet-vim'
  Plugin 'tpope/vim-fugitive'
  Plugin 'vim-airline/vim-airline'
  Plugin 'vim-airline/vim-airline-themes'
  Plugin 'matze/vim-move'
  Bundle 'herrbischoff/cobalt2.vim'
  Plugin 'tpope/vim-surround'
  Plugin 'kien/ctrlp.vim'
  Plugin 'pangloss/vim-javascript'
call vundle#end()

set noundofile
colorscheme cobalt2
set guifont=Consolas:h12

let g:airline_theme='cobalt2'

:set showmatch
:set matchtime=3

autocmd vimenter * NERDTree

let g:move_map_keys = 0
vmap <C-j> <Plug>MoveBlockDown
vmap <C-k> <Plug>MoveBlockUp
nmap <A-j> <Plug>MoveLineDown
nmap <A-k> <Plug>MoveLineUp

let g:ctrlp_cmd = 'CtrlP'