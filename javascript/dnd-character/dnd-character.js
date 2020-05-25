import { runInThisContext } from "vm";

export const abilityModifier = (value) => {
  if (value < 3) throw 'Ability scores must be at least 3';
  if (value > 18) throw 'Ability scores can be at most 18';

  return Math.floor((value - 10) / 2);
};

export class Character {
  constructor() {
    this._strength = Character.rollAbility();
    this._dexterity = Character.rollAbility();
    this._constitution = Character.rollAbility();
    this._intelligence = Character.rollAbility();
    this._wisdom = Character.rollAbility();
    this._charisma = Character.rollAbility();
    
    this._hitpoints = abilityModifier(this._constitution) + 10;
  }

  static rollAbility() {
    return Math.floor(Math.random() * 6) +
      Math.floor(Math.random() * 6) +
      Math.floor(Math.random() * 6);
  }

  get strength() { return this._strength; }

  get dexterity() { return this._dexterity; }

  get constitution() { return this._constitution; }

  get intelligence() { return this._intelligence; }

  get wisdom() { return this._wisdom; }

  get charisma() { return this._charisma; }

  get hitpoints() { return this._hitpoints; }
}