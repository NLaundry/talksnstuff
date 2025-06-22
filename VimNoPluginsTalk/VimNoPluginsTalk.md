# Vim as a full IDE without Plugins

And you thought it couldn't be done. Weak!

---

## Assumptions

- You know the basics of how to use Vim

---

## Basic Usability Config

- First we need reasonable config
- this is pretty minimal

```vimscript
 " Set your configuration to some reasonable defaults
 set nocompatible              

 " Enable line numbers
 set number

 " Enable line indenting
 set autoindent
 set smartindent

 " Enable syntax highlighting
 syntax on

 " Enable search highlighting
 set hlsearch

 " set clipboard=unnamedplus
 set clipboard+=unnamed
```

---

## Windows, Buffers, Splits

---

## Resizing and managing Windows

ctrl-w Then some stuff

---

## The integrated Terminal

```vimscript
:term
```

---

## Netrw - your file explorer

```vimscript
:Ex
```

---

## Making windows feel familiar

Now we have all the ingredients we need to setup a familar window layout
- File Drawer on the left
- integrated terminal at the bottom

---

### File Drawer with NetRW in a window

```vimscript

vnew | Ex | 20wincmd <

```

This pipes 3 commands together
- make a new vertical split
- open the NetRW file explorer
- run the wincmd that reduces the width of the panel 20 times
    -  for some reason you can't do wincmd 30 < like you can <C-w> 30 < but hey, we have ex commands repeat thingy

---

### Integrated terminals

```vimscript
rightbelow sp | 20wincmd - | term ++curwin
```

Similar to the previous one
- this creates a split below
- reduces its size 20 times
- opens a terminal in the current window (without ++curwin neovim will spawn this in a new split instead of the one we just made)


---

## File Navigation: Links, Find, and Path

Vim has surprisingly great tools for file navigation

Find - :find
setpath +=


---

## Session Management

Takes the current set of buffers, tabs, windows, etc. and saves it as a vimcript where you are

#### Create asession

```vimscript
:mksession
```

#### load with
```sh
vim -S Session.vim 
```

---

## Session Automation

