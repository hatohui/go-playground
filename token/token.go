package token

import (
	"fmt"
	"io"
	"strings"
)

type Tokenizer interface {
	Next() (string, error)
	All() ([]string, error)
	Peek() (string, error)
	Reset()
	HasNext() bool
}

func NewTokenizer(input string) (Tokenizer, error) {
	if (strings.TrimSpace(input) == "") {
		return nil, fmt.Errorf("input cannot be empty")
	}
	
	strings := splitTokens(input)

	return &tokenizer{
		tokens: strings,
		index:  0,
	}, nil
}

type tokenizer struct {
	tokens []string
	index  int
}

func (t *tokenizer) All() ([]string, error) {
	return t.tokens, nil
}

func (t *tokenizer) Next() (string, error) {
	if !t.HasNext() {
		return "", io.EOF
	}
	token := t.tokens[t.index]
	t.index++
	return token, nil
}

func (t *tokenizer) Peek() (string, error) {
	if t.index >= len(t.tokens) {
		return "", io.EOF
	}

	return t.tokens[t.index], nil
}

func (t *tokenizer) Reset() {
	t.index = 0
}

func (t *tokenizer) HasNext() bool {
	return t.index < len(t.tokens)
}

func splitTokens(input string) []string {
	trimmed := strings.TrimSpace(input)
	
	if trimmed == "" {
		return nil
	}

	return strings.FieldsFunc(trimmed, func(r rune) bool {
		return r == ' ' || r == ',' || r == ';' || r == '.'
	})
}