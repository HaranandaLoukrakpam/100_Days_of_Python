-- Bootstrap lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

vim.opt.number = true          -- shows actual line number
vim.opt.relativenumber = true  -- shows relative line numbers

-- Plugins
local plugins = {
  { "catppuccin/nvim", name = "catppuccin", priority = 1000 },
  {
    'nvim-telescope/telescope.nvim', version = '*',
    dependencies = {
      'nvim-lua/plenary.nvim',
      { 'nvim-telescope/telescope-fzf-native.nvim', build = 'make' },
    },
  },
  {
    'nvim-treesitter/nvim-treesitter',
    lazy = false,
    build = ':TSUpdate',
  },
  {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
      "nvim-tree/nvim-web-devicons",
    },
    lazy = false,
  },
}

local opts = {}
require("lazy").setup(plugins, opts)

-- Telescope keymaps
local ok_telescope, builtin = pcall(require, "telescope.builtin")
if ok_telescope then
  vim.keymap.set('n', '<C-p>', builtin.find_files, {})
  vim.keymap.set('n', '<leader>fg', builtin.live_grep, {})
end

-- Treesitter
local ok_ts, config = pcall(require, "nvim-treesitter.configs")
if ok_ts then
  config.setup({
    ensure_installed = { "lua", "python", "cpp", "html", "css", "java", "javascript" },
    highlight = { enable = true },
    indent = { enable = true },
  })
end

-- Neo-tree keymap
vim.keymap.set('n', '<C-l>', ':Neotree left reveal toggle<CR>', {})

-- Theme
require("catppuccin").setup()
vim.cmd.colorscheme "catppuccin"
