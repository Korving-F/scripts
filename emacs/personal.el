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
