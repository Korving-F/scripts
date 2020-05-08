;;; Multi-term require -> download multi-term.el in load path dir
(require 'multi-term)
(setq multi-term-program "/bin/bash")

;;; Set ctrl-tab key-binding
(global-set-key (kbd "C-<tab>") 'other-window)
(defun register-keybinds (file)
  (global-set-key (kbd "C-<tab>") 'other-window)
)
(add-hook 'after-load-functions 'register-keybinds)
(register-keybinds nil)

;;; Set ido-mode autocomplete / Disable scroll bar
(custom-set-variables
'(ido-mode (quote both) nil (ido))
 '(scroll-bar-mode nil))

;;; Decrease default font size
(set-face-attribute 'default nil :height 100)

;;; Set line numbers in margin
(global-linum-mode t)

;;; Redefines windmove: not on MATE? delete these!
(global-unset-key (vector (list 'shift 'left)))
(global-unset-key (vector (list 'shift 'right)))
(global-unset-key (vector (list 'shift 'up)))
(global-unset-key (vector (list 'shift 'down)))
(setq shift-selection-mode t)
(setq prelude-guru nil)

;;; Set Tab-Width
(setq tab-width 4)

;; Add melpa package archive
(add-to-list 'package-archives
             '("melpa" . "http://melpa.org/packages/"))

;; Enable neotree (F8) after install
(require 'neotree)
(global-set-key [f8] 'neotree-toggle)

;; Set neotree theme and remove fixed window size
(setq neo-theme (if (display-graphic-p) 'icons 'arrow))
(setq neo-window-fixed-size nil)
(setq-default neo-show-hidden-files t)

;; Enable all-the-icons
(require 'all-the-icons)
