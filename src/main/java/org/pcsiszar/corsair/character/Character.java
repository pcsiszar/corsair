package org.pcsiszar.corsair.character;

import lombok.Builder;
import lombok.Data;
import lombok.Setter;
import org.pcsiszar.corsair.dice.Die;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.LinkedList;
import java.util.stream.Stream;

import org.pcsiszar.corsair.track.ConditionTrack;
import org.pcsiszar.corsair.combat.Attack;

@Data
public class Character {
  private Attribute strength;
  private Attribute agility;
  private Attribute finesse;
  private Attribute knowledge;
  private Attribute presence;
  private Attribute instinct;

  @Setter
  private int damageBonus;
  @Setter
  private int physicalProtection;
  @Setter
  private int mentalProtection;

  private int maxGambitTrackSize = 4;
  private Queue<Die> gambitTrack = new LinkedList<>();

  private final int maxActionTokens;
  private int actionTokens;
  private ConditionTrack physicalTrack;
  private ConditionTrack mentalTrack;

  public int getEndurance() {
    List<Integer> physicalAttrs = Stream.of(strength, agility, finesse)
        .map(Attribute::getValue)
        .sorted()
        .toList();
    return physicalAttrs.get(1);
  }

  public int getWillpower() {
    List<Integer> mentalAttrs = Stream.of(knowledge, presence, instinct)
        .map(Attribute::getValue)
        .sorted()
        .toList();
    return mentalAttrs.get(1);
  }

  public boolean addGambitDie(Die die) {
    if (gambitTrack.size() < maxGambitTrackSize) {
      return gambitTrack.offer(die);
    }
    return false;
  }

  public Die popGambitDie() {
    return gambitTrack.poll();
  }

  public boolean takePhysicalDamage(int amount) {

    return physicalTrack.damage(amount);
  }

  public void healPhysicalDamage(int amount) {
    physicalTrack.heal(amount);
  }

  public boolean takeMentalDamage(int amount) {
    return mentalTrack.damage(amount);
  }

  public void healMentalDamage(int amount) {
    mentalTrack.heal(amount);
  }

  public int getPhysicalProtection() {
    return physicalProtection;
  }

  public int getMentalProtection() {
    return mentalProtection;
  }

  @Builder
  public Character(int str, int agi, int fin, int knw, int pre, int ins, int maxActionTokens) {
    this.strength = new Attribute("Strength", str);
    this.agility = new Attribute("Agility", agi);
    this.finesse = new Attribute("Finesse", fin);
    this.knowledge = new Attribute("Knowledge", knw);
    this.presence = new Attribute("Presence", pre);
    this.instinct = new Attribute("Instinct", ins);
    this.gambitTrack = new LinkedList<>();
    this.maxGambitTrackSize = 4;

    this.physicalTrack = new ConditionTrack(4 + getEndurance());
    this.mentalTrack = new ConditionTrack(4 + getWillpower());
    this.maxActionTokens = maxActionTokens;
  }

  public Attack declareAttack(Character defender, AttributePair attributes) {
    if (this.actionTokens < 2) {
      throw new IllegalStateException("Not enough action tokens to declare an attack.");
    }
    this.actionTokens -= 2;
    return new Attack(this, defender, attributes);
  }

  public int getTotalPhysicalDamage() {
    return physicalTrack.getTracks().stream().mapToInt(org.pcsiszar.corsair.track.Track::getCurrentProgress).sum();
  }

  public int getRemainingPhysicalHp() {
    return physicalTrack.getTracks().stream().mapToInt(org.pcsiszar.corsair.track.Track::getFinalValue).sum() - getTotalPhysicalDamage();
  }
}
