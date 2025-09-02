package org.pcsiszar.corsair.character;

import lombok.Builder;
import lombok.Data;
import org.pcsiszar.corsair.dice.Die;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.LinkedList;
import java.util.stream.Stream;

import org.pcsiszar.corsair.track.ConditionTrack;

@Data
public class Character {
  private Attribute strength;
  private Attribute agility;
  private Attribute finesse;
  private Attribute knowledge;
  private Attribute presence;
  private Attribute instinct;

  private Queue<Die> gambitTrack = new LinkedList<>();
  private int maxGambitTrackSize = 4;
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

  @Builder
  public Character(int str, int agi, int fin, int knw, int pre, int ins) {
    this.strength = new Attribute("Strength", str);
    this.strength = new Attribute("Agility", agi);
    this.strength = new Attribute("Finesse", fin);
    this.strength = new Attribute("Knowledge", knw);
    this.strength = new Attribute("Presence", pre);
    this.strength = new Attribute("Instinct", ins);
    this.gambitTrack = new LinkedList<>();
    this.maxGambitTrackSize = 4;

    this.physicalTrack = new ConditionTrack(4 + getEndurance());
    this.mentalTrack = new ConditionTrack(4 + getWillpower());
  }
}
